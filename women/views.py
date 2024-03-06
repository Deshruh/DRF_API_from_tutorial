from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

# from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from women.models import Women, Category
from women.permissions import IsAdminOrReadOnly
from women.serializers import CategorySerializer, WomenSerializer


class WomenViewSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 4


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = WomenViewSetPagination
    # authentication_classes = (TokenAuthentication,)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
