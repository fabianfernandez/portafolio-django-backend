from django.urls import path

from . import views

urlpatterns = [
    path("", views.MessagesListView.as_view()),
    path("create/", views.MessageCreateView.as_view()),
    path("delete/<pk>/", views.MessageDeleteView.as_view()),
    path("update/<pk>/", views.MessageUpdateView.as_view())
]
