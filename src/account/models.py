import random

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser)


def get_random_number():
    number = random.randrange(0, 100)
    return number


class UserManager(BaseUserManager):
    def create_user(self, email, number=get_random_number(), birthday=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        # if not birthday:
        #     raise ValueError('Users must have a birthday')

        user = self.model(
            number=number,
            birthday=birthday,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, birthday, number=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            birthday,
            number=number,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, birthday=None, number=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            birthday=birthday,
            number=number,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    birthday = models.DateField(verbose_name='birthday', blank=True, null=True)
    number = models.IntegerField(verbose_name='number', blank=True, null=True)
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    objects = UserManager()

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
