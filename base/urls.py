from django.urls import path
from . import views


urlpatterns = [
    # path('', firstView, name='firstView'),
    path('tourList/', views.tourList, name="tour-List"),
    path('tourCreate/', views.tourCreate, name="tour-Craete"),
    path('tourDetail/<str:pk>', views.tourDetail, name="tour-detail"),
    path('tourUpdate/<str:pk>', views.tourUpdate, name="tour-update"),
    path('tourDelete/<str:pk>', views.tourDelete, name="tour-delete"),

]
