from datetime import timedelta
from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def format_duration(self):
        storage_time = self.get_duration()
        delta = timedelta(seconds=storage_time)
        total_seconds = delta.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int(total_seconds % 3600 // 60)
        return f'{hours}ч:{minutes}мин'

    def is_strange(self, minutes=60):
        during = self.get_duration()
        minutes = int(during.seconds) // 60
        return minutes > 60

    def get_duration(self):
        entered_at = localtime(self.entered_at)
        leaved_at = localtime(self.leaved_at)
        delta = leaved_at - entered_at
        return delta.total_seconds()
