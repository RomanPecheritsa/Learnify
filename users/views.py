from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course
from users.models import Payment, Subscription, User
from users.serializers import (PaymentSerializer, SubscriptionSerializer,
                               UserHiddenSerializer, UserSerializer)
from users.services import (convert_rub_to_usd, create_stripe_price,
                            create_stripe_session)


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
        if getattr(self, "swagger_fake_view", False):
            return UserSerializer

        # Обычная логика выполнения
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


class SubscriptionAPIView(APIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def post(self, request, *args, **kwargs):
        user = request.user

        course_id = request.data.get("course_id")
        course_item = get_object_or_404(Course, id=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "Подписка удалена"
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "Подписка добавлена"

        return Response({"message": message}, status=status.HTTP_200_OK)


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)

        amount_in_usd = convert_rub_to_usd(payment.amount)

        course = Course.objects.get(id=payment.course.id)
        name = course.title

        price = create_stripe_price(amount_in_usd, name)

        session_id, payment_link = create_stripe_session(price)

        payment.session_id = session_id
        payment.link = payment_link
        payment.save()
