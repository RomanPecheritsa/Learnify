from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import OrderingFilter

from users.models import Payment, User
from users.serializers import (PaymentSerializer, UserHiddenSerializer,
                               UserSerializer)


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(self.request.data.get("password"))
        user.save()


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserHiddenSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        if serializer.instance != self.request.user:
            raise PermissionDenied("You do not have permission to edit this profile.")

        user = serializer.save()

        new_password = self.request.data.get("password")
        if new_password:
            user.set_password(new_password)
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserHiddenSerializer

    def get_serializer_class(self):
        if self.get_object() == self.request.user:
            return UserSerializer
        return UserHiddenSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserHiddenSerializer

    def perform_destroy(self, instance):
        if instance != self.request.user:
            raise PermissionDenied("You do not have permission to delete this profile.")
        instance.delete()


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ("pay_day",)
    filterset_fields = ("course", "lesson", "pay_method")
