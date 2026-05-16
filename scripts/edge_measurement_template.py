"""Template for repeated edge-inference latency measurements.

Example:
    python scripts/edge_measurement_template.py \
        --command "python run_exported_model.py --config configs/pi4b.yaml" \
        --warmup 20 --repeat 200
"""

from __future__ import annotations

import argparse
import csv
import shlex
import statistics
import subprocess
import time
from pathlib import Path


def run_once(command: str) -> float:
    start = time.perf_counter()
    subprocess.run(shlex.split(command), check=True)
    end = time.perf_counter()
    return (end - start) * 1000.0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--command", required=True, help="Exported inference command")
    parser.add_argument("--warmup", type=int, default=20)
    parser.add_argument("--repeat", type=int, default=200)
    parser.add_argument("--out", default="edge_latency_measurements.csv")
    args = parser.parse_args()

    for _ in range(args.warmup):
        run_once(args.command)

    samples = [run_once(args.command) for _ in range(args.repeat)]
    out = Path(args.out)
    with out.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["run", "latency_ms"])
        for i, value in enumerate(samples, start=1):
            writer.writerow([i, f"{value:.6f}"])

    print(f"n={len(samples)}")
    print(f"mean_ms={statistics.mean(samples):.4f}")
    print(f"median_ms={statistics.median(samples):.4f}")
    print(f"stdev_ms={statistics.stdev(samples) if len(samples) > 1 else 0.0:.4f}")
    print(f"output={out}")


if __name__ == "__main__":
    main()
