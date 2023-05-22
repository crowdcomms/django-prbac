import random
import timeit
from django.test import TestCase
import pytest
from django.contrib.auth.models import User
from django_prbac.models import Role, Grant
from pytest_django.asserts import assertNumQueries
# Create your tests here.

pytestmark = pytest.mark.django_db

def test_user_fixture(user: User):
    assert user.username
    assert user.check_password('1234') is True


def test_direct_grant(user: User):
    role = Role.objects.create(name=user.username, slug=user.username)
    admin = Role.objects.create(name='admin', slug='admin')
    assert role.has_privilege(admin) is False

    Grant.objects.create(from_role=role, to_role=admin)
    assert role.has_privilege(admin)


def test_lookup_caching(user_role):
    admin_role = Role.objects.create(name='admin', slug='admin', parameters=set(['app_id']))
    app_ids = map(str, range(1000))
    grants = [Grant(from_role=user_role, to_role=admin_role, assignment={'report_name': app_id}) for app_id in app_ids]

    def check_grant(app_id):
        return user_role.has_privilege(admin_role.instantiate({'app_id':app_id}))
    
    with assertNumQueries(1):
        check_grant('3')

    with assertNumQueries(0):
        check_grant('3')


