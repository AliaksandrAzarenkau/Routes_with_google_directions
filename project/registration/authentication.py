from rest_framework import authentication, exceptions
import jwt

from django.conf import settings
from .models import User


class CustomUserAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        token = request.COOKIES.get('jwt')


        if not token:
            return None

        try:
            payload = jwt.decode(jwt=token,
                                 key=settings.SECRET_KEY,
                                 algorithms=["HS256"])
        except:
            raise exceptions.AuthenticationFailed("Ошибка авторизации")

        user = User.objects.filter(id=payload.get('id')).first()

        return user, None
