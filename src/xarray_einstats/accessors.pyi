from typing import Any, Literal, overload

import numpy as np
import xarray as xr

from ._types import Dims

class LinAlgAccessor:
    def __init__(self, xarray_obj: xr.DataArray) -> None: ...
    def matrix_transpose(self, dims: Dims = None) -> xr.DataArray: ...
    def matrix_power(self, n: int, dims: Dims = None, **kwargs: Any) -> xr.DataArray: ...
    def matmul(self, other: xr.DataArray, dims: Dims = None, **kwargs: Any) -> xr.DataArray: ...
    def cholesky(self, dims: Dims = None, **kwargs: Any) -> xr.DataArray: ...
    @overload
    def qr(
        self,
        dims: Dims = None,
        *,
        mode: Literal["reduced", "complete", "raw"] = "reduced",
        out_append: str = "2",
        **kwargs: Any,
    ) -> tuple[xr.DataArray, xr.DataArray]: ...
    @overload
    def qr(
        self, dims: Dims = None, *, mode: Literal["r"], out_append: str = "2", **kwargs: Any
    ) -> xr.DataArray: ...
    @overload
    def qr(
        self, dims: Dims = None, *, mode: str = "reduced", out_append: str = "2", **kwargs: Any
    ) -> tuple[xr.DataArray, xr.DataArray] | xr.DataArray: ...
    @overload
    def svd(
        self,
        dims: Dims = None,
        *,
        full_matrices: bool = True,
        compute_uv: Literal[True] = True,
        hermitian: bool = False,
        out_append: str = "2",
        **kwargs: Any,
    ) -> tuple[xr.DataArray, xr.DataArray, xr.DataArray]: ...
    @overload
    def svd(
        self,
        dims: Dims = None,
        *,
        full_matrices: bool = True,
        compute_uv: Literal[False],
        hermitian: bool = False,
        out_append: str = "2",
        **kwargs: Any,
    ) -> xr.DataArray: ...
    @overload
    def svd(
        self,
        dims: Dims = None,
        *,
        full_matrices: bool = True,
        compute_uv: bool = True,
        hermitian: bool = False,
        out_append: str = "2",
        **kwargs: Any,
    ) -> tuple[xr.DataArray, xr.DataArray, xr.DataArray] | xr.DataArray: ...
    def eig(self, dims: Dims = None, **kwargs: Any) -> tuple[xr.DataArray, xr.DataArray]: ...
    def eigh(
        self, dims: Dims = None, *, UPLO: Literal["L", "U"] = "L", **kwargs: Any
    ) -> tuple[xr.DataArray, xr.DataArray]: ...
    def eigvals(self, dims: Dims = None, **kwargs: Any) -> xr.DataArray: ...
    def eigvalsh(
        self, dims: Dims = None, *, UPLO: Literal["L", "U"] = "L", **kwargs: Any
    ) -> xr.DataArray: ...
    def norm(self, dims: Dims = None, *, ord: Any = None, **kwargs: Any) -> xr.DataArray: ...
    def cond(self, dims: Dims = None, *, p: Any = None, **kwargs: Any) -> xr.DataArray: ...
    def det(self, dims: Dims = None, **kwargs: Any) -> xr.DataArray: ...
    def matrix_rank(
        self,
        dims: Dims = None,
        *,
        tol: float | xr.DataArray | None = None,
        rtol: float | xr.DataArray | None = None,
        hermitian: bool = False,
        **kwargs: Any,
    ) -> xr.DataArray: ...
    def slogdet(self, dims: Dims = None, **kwargs: Any) -> tuple[xr.DataArray, xr.DataArray]: ...
    def trace(
        self,
        dims: Dims = None,
        *,
        offset: int = 0,
        dtype: np.typing.DTypeLike | None = None,
        out: np.ndarray | None = None,
        **kwargs: Any,
    ) -> xr.DataArray: ...
    def diagonal(self, dims: Dims = None, *, offset: int = 0, **kwargs: Any) -> xr.DataArray: ...
    def solve(self, db: xr.DataArray, dims: Dims = None, **kwargs: Any) -> xr.DataArray: ...
    def inv(self, dims: Dims = None, **kwargs: Any) -> xr.DataArray: ...
    def pinv(
        self,
        dims: Dims = None,
        *,
        rcond: float | xr.DataArray | None = None,
        rtol: float | xr.DataArray | None = None,
        hermitian: bool = False,
        **kwargs: Any,
    ) -> xr.DataArray: ...

class EinopsAccessor:
    def __init__(self, xarray_obj: xr.DataArray) -> None: ...
    def rearrange(
        self, pattern: str, pattern_in: list[Any] | None = None, **kwargs: Any
    ) -> xr.DataArray: ...
    def reduce(
        self, pattern: str, reduction: str | Any, pattern_in: list[Any] | None = None, **kwargs: Any
    ) -> xr.DataArray: ...
