import dataclasses
import datetime
import jwt
from django.conf import settings
from . import models

from .models import User


@dataclasses.dataclass
class UserDataClass:
    first_name: str
    last_name: str
    email: str
    password: str = None
    id: int = None

    @classmethod
    def from_instance(cls, user):
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            id=user.id,
        )


def create_user(user_dc):
    instance = models.User(
        first_name=user_dc.first_name, last_name=user_dc.last_name, email=user_dc.email
    )
    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return UserDataClass.from_instance(instance)


def user_email_selector(email):
    user = User.objects.filter(email=email).first()

    return user


def create_token(user_id):
    dt = datetime.datetime.now() + datetime.timedelta(days=1)

    payload = dict(
        id=user_id,
        exp=int(dt.timestamp()),
        iat=datetime.datetime.utcnow(),
    )
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

    return token.decode('utf-8')
