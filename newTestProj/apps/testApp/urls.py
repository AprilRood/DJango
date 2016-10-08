from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^update$',views.createAuthor, name="createAuthor"),
    url(r'^add$',views.add, name="addBook")
]
