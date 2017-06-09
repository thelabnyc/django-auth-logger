from django.contrib.auth.signals import user_logged_in, user_login_failed
import logging
import datetime


logger = logging.getLogger(__name__)


# If this gets more complex - maybe consider a class so it can be extended

def get_client_ip(request):
    """ Try to get request's ip address even when behind cdn """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def should_log_user(user):
    if user.is_staff:
        return True
    return False


def build_auth_log_string(message: str, user, request):
    """ Build a string with user and auth info for logging """
    return "{} {} {} {}".format(
        message,
        user,
        get_client_ip(request),
        datetime.datetime.now(),
    )


def handle_user_logged_in(sender, user, request, **kwargs):
    if should_log_user(user):
        log_string = build_auth_log_string(
            "User login successful",
            user,
            request,
        )
        logger.info(log_string)


def handle_user_login_failed(sender, user, request, **kwargs):
    if should_log_user(user):
        log_string = build_auth_log_string(
            "User login failed",
            user,
            request,
        )
        logger.info(log_string)

user_logged_in.connect(handle_user_logged_in)
user_login_failed.connect(handle_user_login_failed)
