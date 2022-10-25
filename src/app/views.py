from flask.views import MethodView
import os
import sys
sys.path.append(".")
from ..infrastructure.controller import APIController


class APIView(MethodView):

    def post(self):
        controller = APIController()
        file = os.path.abspath('src/app/request.json')
        data = controller.process_event(file)
        if data["type"] == "new_publication":
            controller.slack_service_provider.send_message(data["body"], data["to"])
        if data["type"]  == "approved_publication":
            print(type(controller.email_service_provider))
            controller.email_service_provider.send_email(data["body"], data["to"])
        # else:
        #     print(0)



# //
# //{
# //  "type": "new_publication",
# //  "body": "Hello There!",
# //  "to": "C0447N114NP"
# //}

