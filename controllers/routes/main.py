from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    # Downloads
    at.BarChart1.custom.data = [
    {
        "x": "Oct 12",
        "downloads": 8914,
    },
    {
        "x": "Oct 18",
        "downloads": 10248,
    },
    {
        "x": "Oct 31",
        "downloads": 13000,
    }
    ]
    at.BarChart1.custom.legend = {"show": False}
    at.BarChart1.custom.options = {
    "downloads": {
        "animate": True,
        "fill": "#1E40AF",
    }
    }

    # Stars
    at.BarChart3.custom.data = [
    {
        "x": "Oct 12",
        "stars": 109,
    },
    {
        "x": "Oct 18",
        "stars": 182,
    },
    {
        "x": "Oct 31",
        "stars": 226,
    }
    ]
    at.BarChart3.custom.legend = {"show": False}

    # YouTube views
    at.BarChart7.custom.data = [
    {
        "x": "Oct 12",
        "views": 1481,
    },
    {
        "x": "Oct 18",
        "views": 2819,
    },
    {
        "x": "Oct 31",
        "views": 4278,
    }
    ]
    at.BarChart7.custom.legend = {"show": False}
    at.BarChart7.custom.options = {
    "views": {
        "fill": "#F97316",
    }
    }

    # YouTube watch hrs
    at.BarChart6.custom.data = [
    {
        "x": "Oct 12",
        "watch_hrs": 42.8,
    },
    {
        "x": "Oct 18",
        "watch_hrs": 84.6,
    },
    {
        "x": "Oct 31",
        "watch_hrs": 127.3,
    }
    ]
    at.BarChart6.custom.legend = {"show": False}
    at.BarChart6.custom.options = {
    "watch_hrs": {
        "fill": "#7DD3FC",
    },
    }

    # YouTube subscribers
    at.BarChart8.custom.data = [
    {
        "x": "Oct 12",
        "subscribers": 31,
    },
    {
        "x": "Oct 18",
        "subscribers": 47,
    },
    {
        "x": "Oct 31",
        "subscribers": 59,
    }
    ]
    at.BarChart8.custom.legend = {"show": False}
    at.BarChart8.custom.options = {
    "subscribers": {
        "fill": "#E11D48",
    }
    }

    # Slack
    at.BarChart9.custom.data = [
    {
        "x": "Oct 12",
        "slack": 87,
    },
    {
        "x": "Oct 18",
        "slack": 191,
    },
    {
        "x": "Oct 31",
        "slack": 244,
    }
    ]
    at.BarChart9.custom.legend = {"show": False}
    at.BarChart9.custom.options = {
    "slack": {
        "fill": "#2DD4BF",
    }
    }

    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    pass