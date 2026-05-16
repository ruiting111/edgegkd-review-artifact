"""Metric helpers for EdgeGKD-style RUL evaluation."""

from __future__ import annotations

import math
from typing import Iterable


def _as_list(values: Iterable[float]) -> list[float]:
    return [float(v) for v in values]


def rmse(y_true: Iterable[float], y_pred: Iterable[float]) -> float:
    true = _as_list(y_true)
    pred = _as_list(y_pred)
    if len(true) != len(pred):
        raise ValueError("y_true and y_pred must have the same length")
    if not true:
        raise ValueError("at least one sample is required")
    return math.sqrt(sum((p - t) ** 2 for t, p in zip(true, pred)) / len(true))


def mae(y_true: Iterable[float], y_pred: Iterable[float]) -> float:
    true = _as_list(y_true)
    pred = _as_list(y_pred)
    if len(true) != len(pred):
        raise ValueError("y_true and y_pred must have the same length")
    if not true:
        raise ValueError("at least one sample is required")
    return sum(abs(p - t) for t, p in zip(true, pred)) / len(true)


def nasa_asymmetric_score(y_true: Iterable[float], y_pred: Iterable[float]) -> float:
    """NASA C-MAPSS score.

    Positive errors correspond to late RUL predictions and are penalized more
    strongly than conservative early predictions.
    """

    total = 0.0
    for target, prediction in zip(_as_list(y_true), _as_list(y_pred)):
        delta = prediction - target
        if delta < 0:
            total += math.exp(-delta / 13.0) - 1.0
        else:
            total += math.exp(delta / 10.0) - 1.0
    return total
