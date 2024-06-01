from rest_framework import generics
from users.models import User, Account, Fullname
from users.serializers import UserSerializer, AccountSerializer, FullnameSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AccountListAPIView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountCreateAPIView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountUpdateAPIView(generics.UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDestroyAPIView(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class FullnameListAPIView(generics.ListAPIView):
    queryset = Fullname.objects.all()
    serializer_class = FullnameSerializer


class FullnameRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Fullname.objects.all()
    serializer_class = FullnameSerializer


class FullnameCreateAPIView(generics.CreateAPIView):
    queryset = Fullname.objects.all()
    serializer_class = FullnameSerializer


class FullnameUpdateAPIView(generics.UpdateAPIView):
    queryset = Fullname.objects.all()
    serializer_class = FullnameSerializer


class FullnameDestroyAPIView(generics.DestroyAPIView):
    queryset = Fullname.objects.all()
    serializer_class = FullnameSerializer
