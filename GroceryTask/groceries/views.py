from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *

class GroceryItemPagination(PageNumberPagination):       
    page_size = 5

class GroceryItemListAPIView(generics.ListAPIView):

    queryset = GroceryItem.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title','description']
    ordering_fields = ['price','created_at']
    serializer_class = GroceryItemSerializer
    pagination_class = GroceryItemPagination
