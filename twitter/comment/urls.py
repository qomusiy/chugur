from django.urls import path
from .views import SendComment, EditComment, DeleteComment
urlpatterns = [
    path('chat/', SendComment.as_view(), name='sendcomment'),
    path('editcomment/<int:pk>/', EditComment.as_view(), name='editcomment'),
    path('deletecomment/<int:pk>/', DeleteComment.as_view(), name='deletecomment'),
]