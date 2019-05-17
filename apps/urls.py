from django.urls import path
from apps import views


app_name = 'apps'
urlpatterns = [
    path('', views.form_index),
    path('classification/', views.classification),
    path('report/', views.report_svm), 
]