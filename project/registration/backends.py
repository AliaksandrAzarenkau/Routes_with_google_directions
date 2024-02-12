import jwt
from django.conf import settings
from rest_framework import authentication, exceptions

from registration.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        """Проверка на аутентификацию"""
        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            return None

        if len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """Аутентификация"""
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except Exception:
            message = 'Ошибка аутентификации. Невозможно декодировать токен'
            raise exceptions.AuthenticationFailed(message)

        try:
            user = User.objects.get(pk=payload['id'])
        except Exception:
            message = 'Пользователь с таким токеном не найден'
            raise exceptions.AuthenticationFailed(message)

        if not user.is_active:
            message = 'Пользователь неактивен'
            raise exceptions.AuthenticationFailed(message)

        return user, token
