from django.contrib.auth.base_user import BaseUserManager

from pams.users.choice import User_Role


class CustomUserManager(BaseUserManager):
    """Custom user model manager where email is the unique identifier for authentication, instead of username"""

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a superuser with the given email and password
        """
        extra_fields.setdefault("is_admin", True)

        if not extra_fields.get("is_admin"):
            raise ValueError("Superuser must have is_admin=True.")
        return self.create_user(email, password, **extra_fields)


class PatientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User_Role.PATIENT)


class ReceptionistManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(is_receptionist=True)


class DoctorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        print(results)
        return results.filter(user__is_doctor=True)
