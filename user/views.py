from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class UserAPIViewSet(ModelViewSet):

    def list(self, request, *args, **kwargs):
        return Response({'message':'test'})
