from django.shortcuts import render
from django.views import View

from .models import Product

class HomePage(View):
	def get(self, request):
		products = Product.objects.all()
		context = {
			"products": products.order_by("-id")[:6],
			"dells": products.filter(category="dell").order_by("-id")[:7],
			"hps": products.filter(category="hp").order_by("-id")[:7],
			"accessories": products.filter(category="accessory").order_by("-id")[:7],
		}
		return render(request, "core/index.html", context)


class AboutPage(View):
	def get(self, request):
		return render(request, "core/about.html")
	

class ContactPage(View):
	def get(self, request):
		return render(request, "core/contact.html")


class ProductPage(View):
	def get(self, request):
		products = Product.objects.all().order_by("-id")
		context = {
			"products": products,
		}
		return render(request, "core/products1.html", context)


class DellProducts(View):
	def get(self, request):
		products = Product.objects.filter(category="dell").order_by("-id")
		context = {
			"products": products,
		}
		return render(request, "core/dell.html", context)
	

class HPProducts(View):
	def get(self, request):
		products = Product.objects.filter(category="hp").order_by("-id")
		context = {
			"products": products,
		}
		return render(request, "core/hp.html", context)


class ProductDetails(View):
	def get(self, request, pk):
		product = Product.objects.get(id=pk)
		context = {
			"product": product,
		}
		return render(request, "core/single-product.html", context)