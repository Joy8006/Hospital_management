from rest_framework.response import Response
from rest_framework.views import APIView
import logging
from common.utils import HelperMethods


class LoggerAPIView(APIView, HelperMethods):
    """APIView with Logger"""

    info_logger = logging.getLogger('info_logger')
    error_logger = logging.getLogger('error_logger')

    def log_info(self, message):
        print(message)
        self.info_logger.info(message)

    def log_error(self, message, error=None):
        if error:
            message = f"{message}: {str(error)}"
        print(message)
        self.error_logger.error(message, exc_info=True)

    def send_200(self, data):
        return Response(data, 200)

    def send_500(self, message="Something went wrong"):
        data = {
            "message": message
        }
        return Response(data, 500)

    def send_400(self, message="Couldn't find any data", code="UNKNOWN"):
        data = {
            "message": message,
            "code": code
        }
        return Response(data, 400)