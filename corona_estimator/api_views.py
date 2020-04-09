from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from src.estimator import estimator


class EstimationList(generics.ListCreateAPIView):

    def post(self, request):
        estimation = estimator(request.data)
        if estimation:
            return Response(estimation)
        else:
            return Response({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

