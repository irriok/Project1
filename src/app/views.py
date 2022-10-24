import flask
from ..infrastructure.controller import APIController


class APIView(flask.views.MethodView):

    def post(self, request):
        controller = APIController()
        file = 'request.json'
        controller.process_event(request, file)