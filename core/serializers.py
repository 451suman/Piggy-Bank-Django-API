from django.contrib.auth.models import Group, User
from rest_framework import serializers

from core.models import Category, Currency, Transaction


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "name", "code"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class WriteTransactionSerializer(serializers.ModelSerializer):

    currency = serializers.SlugRelatedField(
        slug_field="code", queryset=Currency.objects.all()
    )

    class Meta:
        model = Transaction
        fields = [
            "amount",
            "currency",
            "date",
            "description",
            "category",
            "currency",
        ]


class ReadTransactionSerializer(serializers.ModelSerializer):

    currency = CurrencySerializer()
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = [
            "id",
            "amount",
            "currency",
            "date",
            "description",
            "category",
            "currency",
        ]

        read_only_fields = fields


# class TransactionSerializer(serializers.ModelSerializer):

#     category = CategorySerializer()
#     currency = CurrencySerializer()
#     class Meta:
#         model = Transaction
#         fields = "__all__"


# Which Approach is Better?
# Recommendation: Separate Read and Write Serializers (Option 1)
# The best practice is usually to separate read and write serializers, especially in the following scenarios:

# Different Representations: When you need a simplified input for writing (e.g., SlugRelatedField for currency) and a detailed output for reading (e.g., a nested CurrencySerializer).
# Maintainability: As requirements evolve, having separate serializers allows you to adapt one without affecting the other.
# Clarity: It avoids overloading a single serializer with multiple responsibilities, making your codebase easier to understand and maintain
