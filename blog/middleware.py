from rest_framework.exceptions import APIException, ExceptionHandler
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response

class NotFound(APIException):
    status_code = HTTP_404_NOT_FOUND
    default_detail = 'Not found.'

class CustomExceptionHandler(ExceptionHandler):
    def handle_exception(self, exc, context):
        if isinstance(exc, NotFound):
            # Customize error response
            return Response({'error': '404 Not Found (Custom)'}, status=404)
        # Handle other exceptions as needed

        return super().handle_exception(exc, context)