from django.urls import path

from . import views

urlpatterns = [
    path('api/collection/', views.collection_json, name='api_collection'),
    path('', views.index, name='index'),
    path('collections', views.CollectionList.as_view(), name='collection_list'),
    # path('addperson', views.addperson, name='addperson'),
]
