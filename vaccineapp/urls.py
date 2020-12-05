from django.urls import path

from . import views

urlpatterns = [
    path('api/collection/', views.collection_json, name='api-collection'),
    path('', views.index, name='index'),
    path('collections', views.CollectionList.as_view(), name='collection-list'),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
]
