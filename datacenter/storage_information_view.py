from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visit_peoples = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for person in visit_peoples:
        storage_time = person.get_duration(person)
        entered_at = person.entered_at
        duration = person.format_duration(storage_time)
        about_visit_person = {
            'who_entered': person.passcard,
            'entered_at': entered_at,
            'duration': duration,
        }
        non_closed_visits.append(about_visit_person)
    
    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
