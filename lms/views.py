from rest_framework import viewsets
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from lms.models import Course, Lesson
from lms.paginations import CustomPagination
from lms.serializers import CourseSerializer, LessonSerializer
from lms.tasks import send_course_update_email
from users.models import Subscription
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Course.objects.none()
        if user.groups.filter(name="moderator").exists():
            return Course.objects.all()
        return Course.objects.filter(owner=user)

    def perform_update(self, serializer):
        course = serializer.save()
        subscribers = Subscription.objects.filter(course=course).values_list(
            "user__email", flat=True
        )
        user_emails = list(subscribers)

        send_course_update_email.delay(course.id, course.title, user_emails)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [~IsModerator]
        elif self.action == "destroy":
            self.permission_classes = [IsOwner]
        elif self.action in ["update", "partial_update", "retrieve"]:
            self.permission_classes = [IsModerator | IsOwner]
        else:
            self.permission_classes = [IsOwner]
        return super().get_permissions()


class LessonListCreateAPIView(ListCreateAPIView):
    serializer_class = LessonSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Lesson.objects.none()
        if user.groups.filter(name="moderator").exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=user)

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [~IsModerator, IsOwner]
        else:
            self.permission_classes = [IsModerator | IsOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Lesson.objects.none()
        if user.groups.filter(name="moderator").exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=user)

    def get_permissions(self):
        if self.request.method == "DELETE":
            self.permission_classes = [IsOwner]
        else:
            self.permission_classes = [IsModerator | IsOwner]
        return super().get_permissions()
