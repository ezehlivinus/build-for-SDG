from corona_estimator.middleware import LogMiddleware
from logging import info, log
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
import logging, os, django
from datetime import datetime

from src.estimator import estimator
from buildForSDG.settings import BASE_DIR
logger = logging.getLogger(__name__)
from django.contrib.messages.middleware import MessageMiddleware


class EstimationList(generics.ListCreateAPIView):
    queryset = None
    def post(self, request):
        
        estimation = estimator(request.data)
        if estimation:
            return Response(estimation)
        else:
            return Response({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

