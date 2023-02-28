
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, phone, password, **extra_fields):
        if not username or not email or not phone:
            raise ValueError('username, email and phone must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, email, phone, password, **extra_field):
        extra_field.setdefault('is_superuser', False)
        extra_field.setdefault('is_staff', False)
        return self._create_user(username, email, phone, password, **extra_field)

    def create_superuser(self, username, email, phone, password, **extra_field):
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_staff', True)
        if (extra_field.get('is_superuser') and extra_field.get('is_staff')) is not True:
            raise ValueError('is_superuser must be True')
        return self._create_user(username, email, phone, password, **extra_field)




