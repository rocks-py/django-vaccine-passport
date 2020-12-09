from django.urls import path, include

from . import views

urlpatterns = [
    path('api/person-vaccine/', views.post_person_vaccine, name='api-person-vaccine'),
    path('api/person-vaccine/<int:pk>/', views.person_vaccine_item, name='api-person-vaccine-item'),
    path('api/disease/<int:pk>/', views.disease_json, name='api-disease'),
    path('api/collection/', views.collection_json, name='api-collection'),
    path('', views.index, name='index'),
    path('collections', views.CollectionList.as_view(), name='collection-list'),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
    path('promo', views.promo, name='promo'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
]
