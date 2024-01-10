from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserCreateSerializer


class BaseUserView(APIView):
    permission_classes = [AllowAny]
    serializer_class = None


class CreateUserView(BaseUserView, APIView):
    serializer_class = UserCreateSerializer

    def post(self, request):
        if request.method == 'POST':
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=201)
            return Response(serializer.errors, status=400)


class UpdateUserView(BaseUserView, APIView):
    serializer_class = UserCreateSerializer

    def put(self, request):
        if request.method == 'PUT':
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                self.serializer_class.update(
                                             request,
                                             instance=User.objects.filter(username=(data.get('username'))),
                                             validated_data=data,
                                             )
                return Response({'data': serializer.data}, status=201)
            return Response(serializer.errors, status=400)
