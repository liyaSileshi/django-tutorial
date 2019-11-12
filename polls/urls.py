from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='polls-index'),
    path('<int:pk>/', views.DetailView.as_view(), name='polls-detail'),
    path('<int:pk>/result/', views.ResultsView.as_view(), name='polls-result'),
    path('<int:pk>/vote/', views.vote, name='polls-vote')
]

