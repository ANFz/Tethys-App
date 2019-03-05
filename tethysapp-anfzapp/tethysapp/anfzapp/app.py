from tethys_sdk.base import TethysAppBase, url_map_maker


class Anfzapp(TethysAppBase):
    """
    Tethys app class for The ANFz App.
    """

    name = 'The ANFz App'
    index = 'anfzapp:home'
    icon = 'anfzapp/images/images.jpeg'
    package = 'anfzapp'
    root_url = 'anfzapp'
    color = '#000000'
    description = 'App about me'
    tags = '&quot;Me Stuff&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='anfzapp',
                controller='anfzapp.controllers.home'
            ),
        )

        return url_maps
