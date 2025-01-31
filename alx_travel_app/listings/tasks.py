from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_booking_confirmation_email(to_email, booking_details):
    subject = "Booking Confirmation"
    message = f"Dear user,\n\nYour booking has been confirmed.\n\nDetails: {booking_details}\n\nThank you!"
    from_email = "admin@email.com"

    send_mail(subject, message, from_email, [to_email])
    return f"Email sent to {to_email}"
