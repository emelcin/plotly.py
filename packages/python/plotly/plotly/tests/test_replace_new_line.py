from plotly.tools import _replace_newline
from plotly.tests.utils import TestCaseNoTemplate
from plotly.tools import write_coverage_to_file


class TestReplaceNewline(TestCaseNoTemplate):

    def test_replace_newline_in_dict(self):
        input_dict = {"key1": "value\nwith\nnewlines", "key2": "value without newlines"}
        expected_output = {"key1": "value<br>with<br>newlines", "key2": "value without newlines"}
        self.assertEqual(_replace_newline(input_dict), expected_output)

    def test_replace_newline_in_list(self):
        input_list = ["line1\nline2", "line3"]
        expected_output = ["line1<br>line2", "line3"]
        self.assertEqual(_replace_newline(input_list), expected_output)

    def test_replace_newline_in_string_with_newlines(self):
        input_string = "line1\nline2\nline3"
        expected_output = "line1<br>line2<br>line3"
        with self.assertWarns(Warning):
            self.assertEqual(_replace_newline(input_string), expected_output)

    def test_replace_newline_in_string_without_newlines(self):
        input_string = "line1 line2 line3"
        expected_output = "line1 line2 line3"
        self.assertEqual(_replace_newline(input_string), expected_output)

    def test_replace_newline_in_other_type(self):
        input_number = 12345
        expected_output = 12345
        self.assertEqual(_replace_newline(input_number), expected_output)

def test_print_coverage_to_file():
    write_coverage_to_file(file_path="branch_coverage2.txt")
    