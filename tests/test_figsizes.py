"""Tests for figsizes functionality."""
import matplotlib.pyplot as plt
import pytest

from tueplots import figsizes

full_and_half_columns = pytest.mark.parametrize("column", ["full", "half"])
nrows_all = pytest.mark.parametrize("nrows", [1, 2])
ncols_all = pytest.mark.parametrize("ncols", [1, 2])


@full_and_half_columns
@nrows_all
@ncols_all
def test_icml2022(column, nrows, ncols):
    size = figsizes.icml2022(column=column, nrows=nrows)
    plt.rcParams.update(size)


@full_and_half_columns
@nrows_all
def test_cvpr2022(column, nrows):
    size = figsizes.cvpr2022(column=column, nrows=nrows)
    plt.rcParams.update(size)


@nrows_all
def test_neurips2021(nrows):
    size = figsizes.neurips2021(nrows=nrows)
    plt.rcParams.update(size)


@nrows_all
def test_jmlr2001(nrows):
    size = figsizes.jmlr2001(nrows=nrows)
    plt.rcParams.update(size)


def test_beamer_169():
    size = figsizes.beamer_169()
    plt.rcParams.update(size)
