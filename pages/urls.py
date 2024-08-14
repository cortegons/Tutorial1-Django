from django.urls import path
from .views import homePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView

urlpatterns = [
    path("", homePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("products/", ProductIndexView.as_view(), name="index"),
    path("products/<str:id>", ProductShowView.as_view(), name="show"),
]
