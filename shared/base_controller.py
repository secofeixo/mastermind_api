from fastapi import FastAPI


class BaseController():
    """
    Base Controller using fast api
    """
    def __init__(self):
        self.fastapi_app = None

    def initialize(self, app: FastAPI):
        self.fastapi_app = app
