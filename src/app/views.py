import flask
from ..infrastructure.controller import APIController


class APIView(flask.views.MethodView):

    def post(self, request):
        controller = APIController()
        controller.process_event(request)