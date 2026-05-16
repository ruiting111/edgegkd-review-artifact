"""Statistical helpers for paired model comparisons."""

from __future__ import annotations

import random
from collections.abc import Callable, Iterable

try:
    from scipy.stats import wilcoxon
except Exception:  # pragma: no cover
    wilcoxon = None


Metric = Callable[[list[float], list[float]], float]


def paired_bootstrap_ci(
    y_true: Iterable[float],
    pred_a: Iterable[float],
    pred_b: Iterable[float],
    metric: Metric,
    n_boot: int = 10000,
    alpha: float = 0.05,
    seed: int = 1,
) -> tuple[float, float, float]:
    """Return mean paired improvement and percentile CI for metric(a)-metric(b).

    Positive values mean model A has a larger error/score than model B.
    """

    true = list(map(float, y_true))
    a = list(map(float, pred_a))
    b = list(map(float, pred_b))
    if not (len(true) == len(a) == len(b)):
        raise ValueError("all input arrays must have the same length")
    rng = random.Random(seed)
    n = len(true)
    observed = metric(true, a) - metric(true, b)
    draws = []
    for _ in range(n_boot):
        idx = [rng.randrange(n) for _ in range(n)]
        draws.append(
            metric([true[i] for i in idx], [a[i] for i in idx])
            - metric([true[i] for i in idx], [b[i] for i in idx])
        )
    draws.sort()
    lo = draws[int((alpha / 2) * n_boot)]
    hi = draws[int((1 - alpha / 2) * n_boot)]
    return observed, lo, hi


def wilcoxon_signed_rank(errors_a: Iterable[float], errors_b: Iterable[float]) -> float:
    """Return a paired Wilcoxon p value for per-unit or per-bearing errors."""

    if wilcoxon is None:
        raise RuntimeError("scipy is required for wilcoxon_signed_rank")
    result = wilcoxon(list(errors_a), list(errors_b), zero_method="wilcox")
    return float(result.pvalue)


def holm_correct(p_values: Iterable[float]) -> list[float]:
    """Holm-Bonferroni adjusted p values in the original input order."""

    indexed = sorted((float(p), i) for i, p in enumerate(p_values))
    m = len(indexed)
    adjusted = [0.0] * m
    running_max = 0.0
    for rank, (p_value, original_index) in enumerate(indexed):
        corrected = min(1.0, (m - rank) * p_value)
        running_max = max(running_max, corrected)
        adjusted[original_index] = running_max
    return adjusted
