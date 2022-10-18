from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visit_peoples = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in visit_peoples:
        entered_at = visit.entered_at
        duration = visit.format_duration()
        serialized_visit = {
            'who_entered': visit.passcard,
            'entered_at': entered_at,
            'duration': duration,
        }
        non_closed_visits.append(serialized_visit)

    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
