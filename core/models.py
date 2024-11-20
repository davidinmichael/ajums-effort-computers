from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Category(models.TextChoices):
	dell = "dell", _("Dell")
	hp = "hp", _("HP")
	accessory = "accessory", _("Accessory")
	software = "software", _("Software")
	other = "other", _("Other")


class Availability(models.TextChoices):
	available = "available", _("Available")
	unavailable = "unavailable", _("Unavailable")

class BaseModel(models.Model):
	created_at = models.DateField(default=timezone.now)
	updated_at = models.DateField(auto_now=True)

	class Meta:
		abstract = True

class Product(BaseModel):
	name = models.CharField(max_length=50)
	description = models.TextField()
	price = models.DecimalField()
	front_img = models.ImageField(upload_to="products/", null=True, blank=True)
	back_img = models.ImageField(upload_to="products/", null=True, blank=True)
	status = models.CharField(max_length=50, null=True, blank=True, choices=Availability.choices, default=Availability.available)
	category = models.CharField(max_length=50, null=True, blank=True, choices=Category.choices, default=Category.other)

