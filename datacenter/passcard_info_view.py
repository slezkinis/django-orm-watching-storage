from datacenter.models import Passcard
from datacenter.models import Visit, get_duration
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def format_duration(storage_time):
    parts_time = str(storage_time).split('.')
    duration = parts_time[0]
    return duration


def get_is_strange(during):
    if not during: return
    minutes = int(during.seconds) // 60
    is_strange = False
    is_strange = True if minutes > 60 else False
    return is_strange


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard.objects, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        during = get_duration(visit, True)
        is_strange = get_is_strange(during)
        format_during = format_duration(during)
        if is_strange is None:
            continue
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
