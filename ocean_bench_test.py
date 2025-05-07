# ocean_bench_test.py
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

# 1. 파일 열기
ds = xr.open_dataset("C:/Users/danah/Desktop/dc_obs/dc_obs/2020a_SSH_mapping_NATL60_envisat.nc")

print(ds.variables)
