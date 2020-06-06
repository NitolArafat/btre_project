from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='realtors'),
    # path('/listing', views.listing, name='listing'),
    # path('/search',views.search,name='search')


]




