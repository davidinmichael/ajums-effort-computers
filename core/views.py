from django.shortcuts import render
from django.views import View


class HomePage(View):
	def get(self, request):
		return render(request, "core/index.html")


class AboutPage(View):
	def get(self, request):
		return render(request, "core/about.html")
	

class ContactPage(View):
	def get(self, request):
		return render(request, "core/contact.html")


class ProductPage(View):
	def get(self, request):
		return render(request, "core/products.html")