from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    """
    Custom manager for the CustomAccountManager class.
    """

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        """
        Create a superuser with the given parameters.

        Args:
            email (str): The email address of the superuser.
            user_name (str): The username of the superuser.
            first_name (str): The first name of the superuser.
            password (str): The password of the superuser.
            **other_fields: Additional fields for the superuser.

        Returns:
            User: The created superuser.

        Raises:
            ValueError: If is_staff or is_superuser is not set to True.
        """
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):
        """
        Create a user with the given parameters.

        Args:
            email (str): The email address of the user.
            user_name (str): The username of the user.
            first_name (str): The first name of the user.
            password (str): The password of the user.
            **other_fields: Additional fields for the user.

        Returns:
            User: The created user.

        Raises:
            ValueError: If the email is not provided.
        """
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model for the NewUser class.
    """

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        """
        Return the username of the user.

        Returns:
            str: The username of the user.
        """
        return self.user_name