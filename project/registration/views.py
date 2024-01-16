from django.shortcuts import redirect
from rest_framework import views, response, exceptions, permissions, status, generics
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import UserSerializer
from .services import user_email_selector, create_token
from .authentication import CustomUserAuthentication


class RegistrationAPIVew(views.APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(data={1: 2})


class LoginAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = user_email_selector(email=email)

        if user is None:
            raise exceptions.AuthenticationFailed("Неверный адрес почты")

        if user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Неверный пароль")

        token = create_token(user_id=user.id)
        print(user.id)

        resp = response.Response()

        resp.set_cookie(key='jwt', value=token, httponly=True)

        return resp


class LogoutAPIView(views.APIView):
    authentication_classes = [CustomUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie('jwt')

        resp.data = {'message': 'Успешно'}

        return resp


class GetCurrentUserAPIVew(views.APIView):
    authentication_classes = [CustomUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user

        serializer = self.serializer_class(user)

        return response.Response(serializer.data)
# class RegistrationAPIVew(APIView):
#     permission_classes = [AllowAny]
#     serializer_class = RegistrationSerializer
#
#     def post(self, request):
#         """Регистрация пользователя"""
#         user = request.data.get('user', {})
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class LoginAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     permission_classes = [AllowAny]
#     renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
#     template_name = 'login.html'
#     serializer_class = LoginSerializer
#
#     def post(self, request):
#         """Логинизация пользователя"""
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         if request.accepted_renderer.format == 'html':
#             return redirect('./client_create')
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserSerializer
#
#     def retrieve(self, request, *args, **kwargs):
#         """Преобразование объекта User для последующего возврата"""
#         serializer = self.serializer_class(request.user)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def update(self, request, *args, **kwargs):
#         """Обновление объекта User"""
#         serializer_data = request.data.get('user', {})
#         serializer = self.serializer_class(request.user, data=serializer_data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
