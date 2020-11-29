from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('collections', views.CollectionList.as_view(), name='collection_list'),
    # path('addperson', views.addperson, name='addperson'),
]
