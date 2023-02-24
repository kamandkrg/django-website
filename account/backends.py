from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.db.models import Q


class MyBackend(BaseBackend):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username) | Q(phone=username))
            if user and user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None





