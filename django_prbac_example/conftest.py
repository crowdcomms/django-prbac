import uuid
import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, User
from django_prbac.models import Role

@pytest.fixture()
def user() -> get_user_model():
    UserModel: User = get_user_model()
    return UserModel.objects.create_user(
        username=str(uuid.uuid4()), 
        email=f'{uuid.uuid4()}@example.com',
        password='1234'
    )

@pytest.fixture()
def user_role() -> Role:
    return Role.objects.create(name=str(uuid.uuid4()), slug=str(uuid.uuid4()), description='User Role')