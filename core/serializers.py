from django.contrib.auth.models import Group, User
from rest_framework import serializers

from core.models import Category, Currency, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "groups"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "name", "code"]


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = ["id", "user", "name"]


class WriteTransactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # automaticlly sets the current user as the user field during creating a transaction who is authentication
    currency = serializers.SlugRelatedField(
        slug_field="code", queryset=Currency.objects.all()
    )

    class Meta:
        model = Transaction
        fields = [
            "user",
            "amount",
            "currency",
            "date",
            "description",
            "category",
        ]

    def __init__(self, *args, **kwargs):
        """
        Initializes the WriteTransactionSerializer, setting the queryset for the
        category field to only include categories associated with the current user.
        """
        super().__init__(*args, **kwargs)
        user = self.context["request"].user
        self.fields["category"].queryset = user.categories.all()
        # OR ( both are same )
        # user.categeoy.all is used because in models we have use related_name="categories" in category model foreign key with user
        # self.fields["category"].queryset = Category.objects.filter(user=user)


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]
        read_only_fields = fields


class ReadTransactionSerializer(serializers.ModelSerializer):
    user = ReadUserSerializer()
    currency = CurrencySerializer()
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = [
            "id",
            "user",
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
