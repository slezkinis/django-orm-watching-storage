from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404


def get_duration(person):
    entered_at = localtime(person.entered_at)
    if person.leaved_at:
        leaved_at = person.leaved_at
        return leaved_at - entered_at


def format_duration(storage_time):
    parts_time = str(storage_time).split('.')
    duration = parts_time[0]
    return duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard.objects, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        during = get_duration(visit)
        format_during = format_duration(during)
        minutes = int(during.seconds) // 60
        is_strange = False
        if not during: continue
        is_strange = True if minutes > 60 else False
        about_visit = {
            'entered_at': visit.entered_at,
            'duration': format_during,
            'is_strange': is_strange
        }
        this_passcard_visits.append(about_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
