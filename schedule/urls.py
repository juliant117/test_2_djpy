from django.urls import path
from . import views

#url configuration
app_name="schedule"
urlpatterns = [
    path('home_1/',views.home_1),

    #path("",views.index, name="index"),
    #path("<int:question_id>/",views.detail, name="detail"),
    #---------------------- old form ---------------------------------
    #path("specifics<int:question_id>/",views.detail, name="detail"),
    #path("<int:question_id>/results/",views.results, name="results"),
    #path("<int:question_id>/vote/",views.vote, name="vote"),
    
    #---------------------- new form ---------------------------------
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

]
