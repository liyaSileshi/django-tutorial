from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='polls-index'),
    path('<int:question_id>/', views.detail, name='polls-detail'),
    path('<int:question_id>/result/', views.result, name='polls-result'),
    path('<int:question_id>/vote/', views.vote, name='polls-vote')
]

  