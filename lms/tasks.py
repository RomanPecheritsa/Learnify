from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_course_update_email(course_id, course_title, user_emails):
    subject = f"Обновление курса: {course_title}"
    message = f"Курс '{course_title}' был обновлён. Проверьте материалы!"
    from_email = settings.DEFAULT_FROM_EMAIL

    for email in user_emails:
        send_mail(subject, message, from_email, [email])
    print("Emails sent")
