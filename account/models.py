from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel, generate_product_id


class UserRole(models.TextChoices):
	super_admin = "superadmin", _("Super Admin")
	admin = "admin", _("Admin")
	editor = "editor", _("editor")


class AccountManager(BaseUserManager):
	def create_user(self, email=None, password=None, **extra_fields):
		if not email:
			raise ValueError("Email Address is required.")
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_superuser(self, email=None, password=None, **extra_fields):
		user = self.create_user(email, password, **extra_fields)
		user.is_active = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractUser, BaseModel):
	first_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(max_length=50, null=True, blank=True, unique=True)
	user_id = models.CharField(max_length=50, null=True, blank=True, unique=True)
	role = models.CharField(max_length=50, null=True, blank=True, choices=UserRole.choices)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []
	
	objects = AccountManager()

	def __str__(self):
		return f"{self.first_name} {self.last_name} | {self.role}"
	
	def save(self, *args, **kwargs):
		if not self.user_id:
			self.user_id = generate_product_id(4)
		return super().save(*args, **kwargs)
