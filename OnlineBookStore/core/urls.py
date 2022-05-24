from django.urls import path
from .views import BooksView, JournalsView, BooksModifyView, JournalsModifyView

urlpatterns = [
    path('books/', BooksView.as_view({'get': 'list', 'post': 'create'})),
    path('books/<int:id>/', BooksModifyView.as_view({'put': 'update', 'delete': 'destroy'})),
    path('journals/', JournalsView.as_view({'get': 'list', 'post': 'create'})),
    path('journals/<int:id>/', JournalsModifyView.as_view({'put': 'update', 'delete': 'destroy'})),
]