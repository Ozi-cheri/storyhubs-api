from django.urls import path
from storyhubs_feedbacks import views

urlpatterns = [
    path('storyhubs_feedbacks/', views.StoryhubsFeedbackList.as_view()),
    path('storyhubs_feedbacks/<int:pk>/', views.StoryhubsFeedbackDetail.as_view())
]