import re
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from PIL import Image

import uuid


def generate_product_id(length):
    # TODO: Ensure that the generated product number is unique by checking the database or using an algorithm that
    #  guarantees uniqueness
    return str(uuid.uuid4()).replace('-', "").upper()[:length]

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
	price = models.DecimalField(decimal_places=2, max_digits=10)
	front_img = models.ImageField(upload_to="products/", null=True, blank=True)
	back_img = models.ImageField(upload_to="products/", null=True, blank=True)
	status = models.CharField(max_length=50, null=True, blank=True, choices=Availability.choices, default=Availability.available)
	category = models.CharField(max_length=50, null=True, blank=True, choices=Category.choices, default=Category.other)
	product_id = models.CharField(max_length=20, null=True, blank=True, unique=True)
	added_by = models.ForeignKey("account.Account", on_delete=models.SET_NULL, null=True, blank=True, related_name="added_by")
	updated_by = models.ForeignKey("account.Account", on_delete=models.SET_NULL, null=True, blank=True, related_name="updated_by")

	def __str__(self):
		return f"{self.name} | {self.price}"
	
	def save(self, *args, **kwargs):
		if not self.product_id:
			self.product_id = generate_product_id(10)
		super().save(*args, **kwargs)

		if self.front_img:
			self.process_image(self.front_img.path)
		if self.back_img:
			self.process_image(self.back_img.path)

	def process_image(self, image_path):
		with Image.open(image_path) as img:
			if img.height > 390 or img.width > 370:
				output_size = (390, 370)
				img.thumbnail(output_size)
				img.save(image_path)

