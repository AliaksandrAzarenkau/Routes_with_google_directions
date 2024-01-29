from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.views.generic import base
from rest_framework import views, response, exceptions, permissions, status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer

from .serializers import UserSerializer, LoginSerializer, UserRegisterSerializer, UserEditProfileSerializer, \
    UserPhotoProfileSerializer
from .services import user_email_selector, create_token
from .authentication import CustomUserAuthentication
from .models import User, UserProfilePhoto


class RegistrationAPIVew(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        """Получение данных для формы регистрации"""
        queryset = self.queryset

        if request.accepted_renderer.format == 'html':
            serializer = self.serializer_class()
            context = {'clients': queryset, 'serializer': serializer}
            return response.Response(context, template_name=self.template_name)
        else:
            serializer = self.serializer_class(queryset, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Регистрация пользователя"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if request.accepted_renderer.format == 'html':
            message = "Регистрация пройдена успешно"
            messages.success(request, message)
            return redirect('./login')

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'login.html'
    serializer_class = LoginSerializer

    def get(self, request, *args, **kwargs):
        """Получение данных пользователей"""
        queryset = self.queryset

        if request.accepted_renderer.format == 'html':
            serializer = self.serializer_class()
            context = {'user': queryset, 'serializer': serializer}
            return response.Response(context, template_name=self.template_name)
        else:
            return response.Response(status=status.HTTP_200_OK)

    def post(self, request):
        """Авторизация и аутентификация"""
        email = request.data['email']
        password = request.data['password']

        user = user_email_selector(email=email)

        if user is None:
            raise exceptions.AuthenticationFailed("Неверный адрес почты")

        if user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Неверный пароль")

        token = create_token(user_id=user.id)

        authenticate(request, username=email, password=password)

        if user and user.is_active:
            login(request, user)

        if request.accepted_renderer.format == 'html':
            resp = HttpResponseRedirect(redirect_to='./home')
            resp.set_cookie(key='jwt', value=token)
            return resp
        else:
            resp = response.Response()
            resp.set_cookie(key='jwt', value=token)
            return resp


class LogoutAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'logout.html'
    serializer_class = LoginSerializer

    def get(self, request, *args, **kwargs):
        """Получение данных пользователя"""
        queryset = self.queryset

        if request.accepted_renderer.format == 'html':
            serializer = self.serializer_class()
            context = {'user': queryset, 'serializer': serializer}
            return response.Response(context, template_name=self.template_name)
        else:
            return response.Response(status=status.HTTP_200_OK)

    def post(self, request):
        """Выход из профиля"""
        resp = response.Response()

        resp.data = {'message': 'Успешно'}

        if request.accepted_renderer.format == 'html':
            resp = HttpResponseRedirect(redirect_to='./home')
            resp.delete_cookie('jwt')
            logout(request)

            return resp

        resp.delete_cookie('jwt')
        logout(request)

        return resp


class GetCurrentUserAPIVew(views.APIView):
    authentication_classes = [CustomUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        """Получение информации о текущем пользователе"""
        user = request.user

        serializer = self.serializer_class(user)

        return response.Response(serializer.data)


class HomePageView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        """Получение данных пользователей"""
        queryset = self.queryset

        if request.accepted_renderer.format == 'html':
            serializer = self.serializer_class()
            context = {'user': queryset, 'serializer': serializer}
            return response.Response(context, template_name=self.template_name)
        else:
            return response.Response(status=status.HTTP_200_OK)

    def post(self, request):
        return response.Response(request)


class UserEditProfileAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserEditProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'user_profile.html'

    def get(self, request, *args, **kwargs):
        """Получение данных профиля текущего пользователя для заполнения шаблона"""
        user = request.user
        if request.accepted_renderer.format == 'html':
            serializer = self.serializer_class(user)
            context = {'user': user, 'serializer': serializer}
            return response.Response(context, template_name=self.template_name)
        else:
            return response.Response(status=status.HTTP_200_OK)

    def post(self, request):
        """Перемычка"""
        return self.update(request)

    def update(self, request, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=request.user.id)
        serializer = self.serializer_class(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if request.accepted_renderer.format == 'html':
            message = "Данные обновлены успешно"
            messages.success(request, message)
            return redirect('./user_profile')
        else:
            return response.Response(status=status.HTTP_200_OK)


# class UserPhotoAPIView(generics.RetrieveUpdateAPIView):
#     queryset = UserProfilePhoto.objects.all()
#     serializer_class = UserPhotoProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
#     template_name = 'user_profile.html'
#
#     def get(self, request, *args, **kwargs):
#         """Получение фото текущего пользователя для заполнения шаблона"""
#         pk = request.user.id
#         profile_photo = self.serializer_class.get_photo(request, pk)
#         return profile_photo
# serializer = self.serializer_class(request)
# if request.accepted_renderer.format == 'html':
#     context = {'user': request, 'serializer': serializer}
#     return response.Response(context)
# else:
#     return response.Response(serializer, status=status.HTTP_200_OK)

# def post(self, request):
#     """Перемычка"""
#     return self.update(request)
#
# def update(self, request, *args, **kwargs):
#     instance = get_object_or_404(self.queryset, pk=request.user.email_id)
#     serializer = self.serializer_class(instance=instance, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#
#     if request.accepted_renderer.format == 'html':
#         message = "Фото обновлено успешно"
#         messages.success(request, message)
#         return redirect('./user_profile')
#     else:
#         return response.Response(status=status.HTTP_200_OK)

class UserPhotoView(base.View):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def get(self, request):
        resp = UserPhotoProfileSerializer.get_photo(request, request.user.id)

        return HttpResponse(resp)
