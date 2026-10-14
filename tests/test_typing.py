"""Static checks for the public typing surface."""

from typing import assert_type

import numpy as np
import xarray as xr

from xarray_einstats import Dims
from xarray_einstats.accessors import LinAlgAccessor


def test_linalg_accessor_types() -> None:
    da = xr.DataArray(np.eye(3), dims=("row", "col"))
    accessor = LinAlgAccessor(da)
    dims: Dims = ("row", "col")

    assert_type(accessor.inv(dims=dims), xr.DataArray)
    assert_type(accessor.svd(dims=dims), tuple[xr.DataArray, xr.DataArray, xr.DataArray])
    assert_type(accessor.svd(dims=dims, compute_uv=False), xr.DataArray)
    assert_type(accessor.qr(dims=dims, mode="r"), xr.DataArray)
    assert_type(accessor.qr(dims=dims), tuple[xr.DataArray, xr.DataArray])
    assert_type(accessor.matrix_rank(dims=dims, rtol=1e-8), xr.DataArray)
    assert_type(accessor.pinv(dims=dims, rtol=1e-8), xr.DataArray)
