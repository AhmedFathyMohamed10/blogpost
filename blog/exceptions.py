from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        if isinstance(exc, ValueError):  # ممكن تغير الخطأ حسب الحالة
            return Response({'error': 'Invalid path', 'status': status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        # ممكن تضيف أي حالات أخرى تحب تخصصها
    return response
    


   