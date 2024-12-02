from django.shortcuts import render

from rest_framework.generics import ListAPIView

from core.models import Category, Currency, Transaction
from core.serializers import (
    CategorySerializer,
    CurrencySerializer,
    ReadTransactionSerializer,
    WriteTransactionSerializer,
)
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from core.serializers import GroupSerializer, UserSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CurrencyList(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TransactionModelViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["description", "currency__name"]
    filterset_fields = ["currency__code"]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (
            Transaction.objects.select_related("currency", "category", "user")
            .filter(user=self.request.user)
            .order_by("-id")
        )

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ReadTransactionSerializer
        return WriteTransactionSerializer
