# EdgeGKD Review Artifact

This repository provides the review artifact package for the manuscript
`EdgeGKD: Relation-Preserving Graph Knowledge Distillation for Real-Time
Industrial Equipment Health Prediction`.

The package is organized to make the experimental protocol auditable during
review. It records the dataset sources, preprocessing and split decisions,
metric definitions, statistical comparison protocol, and edge-device
measurement protocol used by the manuscript.

## Contents

- `configs/edgegkd_protocol.yaml`: dataset, split, graph-construction,
  training, evaluation, and deployment settings reported in the manuscript.
- `data/README.md`: public dataset sources and expected local data layout.
- `scripts/metrics.py`: RMSE, MAE, and NASA asymmetric score definitions.
- `scripts/stat_tests.py`: paired bootstrap confidence intervals and
  Wilcoxon/Holm testing helpers.
- `scripts/edge_measurement_template.py`: repeatable latency/energy
  measurement template for exported edge inference commands.
- `protocols/edge_measurement.md`: hardware and software fields that should be
  reported with Raspberry Pi 4B and Jetson Nano measurements.

## Dataset Access

The manuscript uses only public benchmark datasets:

- NASA C-MAPSS turbofan degradation data.
- IEEE PHM 2012 / PRONOSTIA bearing degradation benchmark.

Raw datasets are not redistributed in this repository. Download locations and
expected folder names are listed in `data/README.md`.

## Reproduction Scope

This review artifact is intended to support checking the experimental protocol
and the reported metrics. Trained model checkpoints and complete training logs
should be added before final archival release.

## Anonymity Note

The artifact contents avoid author names and institutional identifiers so that
the same repository can be served through an anonymous GitHub proxy for review
if the venue requires a double-anonymous workflow.
