from django import forms
from .models import Product


class AddProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = [
			"name",
			"description",
			"price",
			"front_img",
			"back_img",
			"status",
			"category",
		]