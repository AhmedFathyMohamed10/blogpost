from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status 

def custom_exception_handler(exc, context):
    if isinstance(exc, NotFound):
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return None


