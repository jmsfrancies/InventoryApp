"""A dashboardController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class dashboardController(Controller):
    """dashboardController Controller Class."""

    def __init__(self, request: Request):
        """dashboardController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        return view.render('dashboard')
