from django.urls import path
from . import views


 # LOCAL HOST - 8000/chai
urlpatterns = [
    path('', views.all_chai, name="all_chai"),
    path('<int:chai_id>/', views.chai_detail, name="chai_detail"),
    
]
