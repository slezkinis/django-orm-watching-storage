from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard.objects, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        during = visit.get_duration()
        is_strange = visit.get_is_strange(during)
        format_during = visit.format_duration(during)
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
