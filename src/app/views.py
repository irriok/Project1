from flask.views import MethodView
import os
import sys
sys.path.append(".")
from ..infrastructure.controller import APIController


class APIView(MethodView):

    def post(self):
        controller = APIController()
        file = os.path.abspath('src/app/request.json')
        controller.process_event(file)




# //
# //{
# //  "type": "new_publication",
# //  "body": "Hello There!",
# //  "to": "C0447N114NP"
# //}

