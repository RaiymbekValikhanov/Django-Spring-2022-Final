from django.shortcuts import render
from rest_framework import status, pagination, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer
# Create your views here.

class BooksView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = BookSerializer
    lookup_field = 'id'
    queryset = Book.objects.all()


class BooksModifyView(BooksView):
    permission_classes = (IsAdminUser, )


class JournalsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = JournalSerializer
    lookup_field = 'id'
    queryset = Journal.objects.all()

class JournalsModifyView(JournalsView):
    permission_classes = (IsAdminUser, )
