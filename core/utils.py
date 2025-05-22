from datetime import timedelta
from django.utils import timezone
from .models import Kudos

def start_of_week():
    now = timezone.now()
    return now - timedelta(days=now.weekday())

def kudos_given_this_week(user):
    return Kudos.objects.filter(sender=user, timestamp__gte=start_of_week())

def kudos_remaining(user):
    return max(0, 3 - kudos_given_this_week(user).count())

def can_give_kudos(sender, receiver):
    if sender == receiver:
        return False, "You cannot send kudos to yourself."
    if sender.organization != receiver.organization:
        return False, "Users must be in the same organization."
    if kudos_remaining(sender) <= 0:
        return False, "No kudos remaining this week."
    return True, ""
