import pytest
import numpy as np
from plotly.express._imshow import _vectorize_zvalue, branch_coverage, print_coverage_to_file

def test__vectorize_zvalue_None_ReturnsNone():
    assert _vectorize_zvalue(None) is None
    assert branch_coverage["_vectorize_zvalue_none"]

def test__vectorize_zvalue_Scalar5_ReturnsListWithAlpha():
    assert _vectorize_zvalue(5) == [5, 5, 5, 255]
    assert branch_coverage["_vectorize_zvalue_scalar"]

def test__vectorize_zvalue_Length1List_ReturnsListWithAlpha():
    assert _vectorize_zvalue([5]) == [5, 5, 5, 255]
    assert branch_coverage["_vectorize_zvalue_len_1"]

def test__vectorize_zvalue_Length3List_ReturnsListWithAlpha():
    assert _vectorize_zvalue([1, 2, 3]) == [1, 2, 3, 255]
    assert branch_coverage["_vectorize_zvalue_len_3"]

def test__vectorize_zvalue_Length4List_ReturnsSameList():
    assert _vectorize_zvalue([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert branch_coverage["_vectorize_zvalue_len_4"]

def test__vectorize_zvalue_InvalidLength_ThrowsValueError():
    with pytest.raises(ValueError):
        _vectorize_zvalue([1, 2])
    assert branch_coverage["_vectorize_zvalue_else"]

def test_print_coverage_to_file():
    print_coverage_to_file('coverage.txt')