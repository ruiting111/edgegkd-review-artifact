# Public Data Sources

## NASA C-MAPSS

Use the Turbofan Engine Degradation Simulation Data Set from the NASA Prognostics
Data Repository / PHM Society mirror.

Expected local layout:

```text
data/
  raw/
    cmapss/
      train_FD001.txt
      test_FD001.txt
      RUL_FD001.txt
      ...
      train_FD004.txt
      test_FD004.txt
      RUL_FD004.txt
```

Protocol summary:

- Retain sensors 2, 3, 4, 7, 8, 9, 11, 12, 13, 14, 15, 17, 20, and 21.
- Remove near-constant or non-informative sensor channels.
- Use the three operating-setting variables for normalization and
  operating-regime handling.
- Convert each engine trajectory into overlapping windows of length 30 with
  stride 1.
- Cap RUL labels at 125 cycles and normalize labels for training.
- Select 20% of official training engines as validation engines at the unit
  level. Do not split windows from the same engine across train/validation.
- Use official test units only for final evaluation.

## IEEE PHM 2012 / PRONOSTIA

Use the accelerated bearing degradation records from the IEEE PHM 2012 data
challenge / PRONOSTIA benchmark.

Expected local layout:

```text
data/
  raw/
    phm2012/
      Bearing1_1/
      Bearing1_2/
      ...
      Bearing3_3/
```

Protocol summary:

- Training bearings: Bearing1_1, Bearing2_1, Bearing3_1.
- Validation bearings: Bearing1_2, Bearing2_2, Bearing3_2.
- Test bearings: Bearing1_3--Bearing1_7, Bearing2_3--Bearing2_7, Bearing3_3.
- Process each 2560-sample vibration record chronologically.
- Compute time-domain statistics and frequency-domain descriptors from the
  single-sided FFT magnitude after a Hann window.
- Feature channels are graph nodes.
- Normalize features using training-bearing statistics only.
- Use normalized remaining lifetime as the target, y_t = (T - t) / T.
