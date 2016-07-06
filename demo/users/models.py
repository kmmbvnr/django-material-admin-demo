from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible



class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, identifier, password=None, **extra_fields):
        user = self.model(identifier=identifier)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, identifier, password, **extra_fields):
        user = self.model(identifier=identifier, is_staff=True, is_superuser=True)
        user.set_password(password)
        user.save(using=self._db)
        return user


@python_2_unicode_compatible
class User(AbstractBaseUser, PermissionsMixin):
    identifier = models.CharField(max_length=40, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'identifier'

    objects = UserManager()

    def __str__(self):
        return self.identifier

    def get_full_name(self):
        return self.identifier

    def get_short_name(self):
        return self.identifier
