from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.db.models import Q

User = get_user_model()

class MyBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        print(111111111111111111111111111112222222222222222)
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





