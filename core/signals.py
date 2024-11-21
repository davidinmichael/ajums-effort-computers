from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Product


@receiver(post_save, sender=Product)
def resize_image(sender, instance, created, **kwargs):
	if created:
		if instance.front_img:
			instance.process_image(instance.front_img.path)
		if instance.back_img:
			instance.process_image(instance.back_img.path)