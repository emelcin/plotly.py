import pytest
from plotly.figure_factory.utils import annotation_dict_for_label, branch_coverage_annotation, print_coverage_to_file

def test_not_flipped_col():
    annotation_dict_for_label("text", 1, 3, 0.1, row_col="col", flipped=False)
    assert branch_coverage_annotation["not_flipped_col"]

def test_not_flipped_row():
    annotation_dict_for_label("text", 1, 3, 0.1, row_col="row", flipped=False)
    assert branch_coverage_annotation["not_flipped_row"]

def test_flipped_col():
    annotation_dict_for_label("text", 1, 3, 0.1, row_col="col", flipped=True)
    assert branch_coverage_annotation["flipped_col"]

def test_flipped_row_right_side():
    annotation_dict_for_label("text", 1, 3, 0.1, row_col="row", flipped=True, right_side=True)
    assert branch_coverage_annotation["flipped_row_right_side"]

def test_flipped_row_left_side():
    annotation_dict_for_label("text", 1, 3, 0.1, row_col="row", flipped=True, right_side=False)
    assert branch_coverage_annotation["flipped_row_left_side"]

def test_flipped_row():
    annotation_dict_for_label("text", 1, 3, 0.1, row_col="row", flipped=True, right_side=True)
    assert branch_coverage_annotation["flipped_row_right_side"]
    annotation_dict_for_label("text", 1, 3, 0.1, row_col="row", flipped=True, right_side=False)
    assert branch_coverage_annotation["flipped_row_left_side"]

def test_print_coverage_to_file():
    print_coverage_to_file('coverage.txt')