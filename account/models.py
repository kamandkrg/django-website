from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from account.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    MALE = "M"
    FEMALE = "F"
    UNSURE = "U"
    SEX_CHOICE = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNSURE, 'Unsure')
    )
    username = models.CharField(max_length=32, unique=True, null=True)
    phone = PhoneNumberField(null=True, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICE, default=UNSURE, null=True, blank=True)
    national_code = models.PositiveBigIntegerField(null=True, blank=True)
    job = models.CharField(max_length=124, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

