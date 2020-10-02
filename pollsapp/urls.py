from django.urls import path

from . import views

app_name = 'pollsapp'

urlpatterns = [
    # ex: /pollsapp/
    path('', views.index, name='index'),
    # ex: /pollsapp/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /pollsapp/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /pollsapp/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]