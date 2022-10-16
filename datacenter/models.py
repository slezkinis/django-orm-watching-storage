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


    def format_duration(self, storage_time):
        parts_time = str(storage_time).split('.')
        duration = parts_time[0]
        return duration
    

    def get_is_strange(self, minutes=60):
        during = self.get_duration(True)
        minutes = int(during.seconds) // 60
        return minutes > 60


    def get_duration(self, variable_can_empty=False):
        entered_at = localtime(self.entered_at)
        if variable_can_empty:
            if self.leaved_at:
                leaved_at = self.leaved_at
                return leaved_at - entered_at
        else:
            local_time = localtime()
            return local_time - entered_at
    
