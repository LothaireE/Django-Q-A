from django.urls import path
from .views import list_info, question_list, question_details, register, create_question, update_question, delete_question, update_answer, delete_answer, HomeView, change_profile

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('question/', question_list, name='qlist'),
    path('question/<slug:slug>/', question_details, name='qdetails'),
    path('register/', register, name='register'),
    path('add-question/', create_question, name='create_question'),
    path('question/update/<slug:slug>/', update_question, name='update_question'),
    path('question/delete/<slug:slug>/', delete_question, name='delete_question'),
    path('answer/update/<int:id>/', update_answer, name='update_answer'),
    path('answer/delete/<int:id>/', delete_answer, name='delete_answer'),
    path('profile/', change_profile, name='profile'),
    path('list/', list_info, name='list'),


]