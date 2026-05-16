# Edge Measurement Protocol Fields

The following fields should be recorded for each reported latency and energy
measurement.

## Hardware

- Device name and revision.
- RAM capacity.
- Storage medium.
- Power supply rating.
- Cooling condition.
- Ambient temperature.

## Software

- Operating system image and kernel version.
- Python version.
- Inference runtime, for example PyTorch, ONNX Runtime, TensorFlow Lite, or
  another exported runtime.
- Runtime version.
- BLAS / acceleration backend.
- Thread count and CPU affinity.
- CPU governor and fixed-frequency setting, if used.

## Latency

- Batch size.
- Number of warm-up runs.
- Number of measured runs.
- Timer API.
- Whether input normalization is included.
- Whether graph construction is included.
- Whether readout and post-processing are included.
- Mean, median, standard deviation, and percentile latencies.

## Energy

- Power meter model.
- Sampling rate.
- Idle-power estimation procedure.
- Synchronization between inference window and power trace.
- Active-power integration method.
- Whether reported energy is absolute or comparative.
