from django.urls import path
from .views import HomePage, AboutPage, ContactPage, ProductPage, DellProducts, HPProducts, ProductDetails, AddProducts, Accessories
urlpatterns = [
	path("", HomePage.as_view(), name = "home"),
	path("about/", AboutPage.as_view(), name = "about"),
	path("contact/", ContactPage.as_view(), name = "contact"),
	path("products/", ProductPage.as_view(), name = "products"),
	path("dell/", DellProducts.as_view(), name = "dell"),
	path("hp/", HPProducts.as_view(), name = "hp"),
	path("accessories/", Accessories.as_view(), name = "accessories"),
	path("product/<str:pk>/", ProductDetails.as_view(), name = "product-details"),
	path("add-product/", AddProducts.as_view(), name = "add_product"),
]
