from django.urls import include, path
from .views import NoteGet, NotePost, NotePut, NoteDelete, NoteViewSet, NotesGet

urlpatterns = [
    path('', NotesGet.as_view(), name='retrieve-notes'),
    path('create/', NotePost.as_view(), name='create-note'),
    path('<int:pk>/', NoteGet.as_view(), name='retrieve-note'),
    path('update/<int:pk>/', NotePost.as_view(), name='update-note'),
    path('delete/<int:pk>/', NoteDelete.as_view(), name='delete-note')
]
