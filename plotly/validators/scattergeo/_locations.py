import _plotly_utils.basevalidators


class LocationsValidator(_plotly_utils.basevalidators.DataArrayValidator):

    def __init__(
        self, plotly_name='locations', parent_name='scattergeo', **kwargs
    ):
        super(LocationsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='data',
            **kwargs
        )