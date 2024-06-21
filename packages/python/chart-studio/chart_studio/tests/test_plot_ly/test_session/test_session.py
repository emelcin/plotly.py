from __future__ import absolute_import

from chart_studio.tests.utils import PlotlyTestCase

from chart_studio import session
from chart_studio.session import update_session_plot_options, SHARING_OPTIONS
from _plotly_utils.exceptions import PlotlyError
from chart_studio.session import sign_in, get_session_credentials, get_session_config


class TestSession(PlotlyTestCase):
    def setUp(self):
        super(TestSession, self).setUp()
        session._session["plot_options"].clear()

    def test_update_session_plot_options_invalid_sharing_argument(self):

        # Return PlotlyError when sharing arguement is not
        # 'public', 'private' or 'secret'

        kwargs = {"sharing": "priva"}
        self.assertRaises(PlotlyError, update_session_plot_options, **kwargs)

    def test_update_session_plot_options_valid_sharing_argument(self):

        # _session['plot_options'] should contain sharing key after
        # update_session_plot_options is called by correct arguments
        # 'public, 'private' or 'secret'
        from chart_studio.session import _session

        for key in SHARING_OPTIONS:
            kwargs = {"sharing": key}
            update_session_plot_options(**kwargs)

            self.assertEqual(_session["plot_options"], kwargs)

class Testing(PlotlyTestCase):
    def set_up(self):
        super(TestSession, self).setUp()
        session._session["credentials"].clear()
        session._session["config"].clear()
        session._session["plot_options"].clear()

    def test_sign_in_valid_credentials(self):
        sign_in(username="test_user", api_key="test_key")
        credentials = get_session_credentials()
        self.assertEqual(credentials["username"], "test_user")
        self.assertEqual(credentials["api_key"], "test_key")

    def test_sign_in_invalid_key(self):
        with self.assertRaises(PlotlyError) as context:
            sign_in(username="test_user", api_key="test_key", invalid_key="value")
        self.assertEqual(
            str(context.exception), "invalid_key is not a valid config or credentials key"
        )

    def test_sign_in_invalid_credentials_type(self):
        with self.assertRaises(PlotlyError) as context:
            sign_in(username="test_user", api_key=12345)
        self.assertEqual(
            str(context.exception), "api_key must be of type '<class 'str'>'"
        )

    def test_sign_in_valid_config(self):
        sign_in(username="test_user", api_key="test_key", plotly_domain="https://plotly.com")
        config = get_session_config()
        self.assertEqual(config["plotly_domain"], "https://plotly.com")

    def test_sign_in_invalid_config_type(self):
        with self.assertRaises(PlotlyError) as context:
            sign_in(username="test_user", api_key="test_key", plotly_ssl_verification="yes")
        self.assertEqual(
            str(context.exception), "plotly_ssl_verification must be of type '<class 'bool'>'"
        )

    def test_sign_in_partial_update(self):
        sign_in(username="test_user", api_key="test_key")
        sign_in(username="new_user")
        credentials = get_session_credentials()
        self.assertEqual(credentials["username"], "new_user")
        self.assertEqual(credentials["api_key"], "test_key")

    def test_sign_in_valid_plot_options(self):
        sign_in(username="test_user", api_key="test_key", filename="test_file")
        plot_options = session._session["plot_options"]
        self.assertEqual(plot_options["filename"], "test_file")

    def test_sign_in_invalid_plot_options_type(self):
        with self.assertRaises(PlotlyError) as context:
            sign_in(username="test_user", api_key="test_key", filename=123)
        self.assertEqual(
            str(context.exception), "filename must be of type '<class 'str'>'"
        )
