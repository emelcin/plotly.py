from __future__ import absolute_import

from chart_studio.tests.utils import PlotlyTestCase

from chart_studio.utils import is_source_key, print_coverage_to_file_source_key, branch_coverage


class TestIsSourceKey(PlotlyTestCase):

    def test_key_ends_with_src(self):
        self.assertTrue(is_source_key("datasrc"))

    def test_key_does_not_end_with_src(self):
        self.assertFalse(is_source_key("data"))
    
    def test_print_coverage_to_file_source_key(self):
        print_coverage_to_file_source_key('coverage1.txt')
