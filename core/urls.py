from django.urls import path
from .views import HomePage, AboutPage, ContactPage, ProductPage, DellProducts, HPProducts


urlpatterns = [
	path("", HomePage.as_view(), name = "home"),
	path("about/", AboutPage.as_view(), name = "about"),
	path("contact/", ContactPage.as_view(), name = "contact"),
	path("products/", ProductPage.as_view(), name = "products"),
	path("dell/", DellProducts.as_view(), name = "dell"),
	path("hp/", HPProducts.as_view(), name = "hp"),
]
