from datacenter.models import Visit
from datacenter.models import get_duration
from django.shortcuts import render


def format_duration(storage_time):
    parts_time = str(storage_time).split('.')
    duration = parts_time[0]
    return duration


def storage_information_view(request):
    visit_peoples = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for person in visit_peoples:
        storage_time = get_duration(person)
        entered_at = person.entered_at
        duration = format_duration(storage_time)
        about_visit_person = {
            'who_entered': person.passcard,
            'entered_at': entered_at,
            'duration': duration,
        }
        non_closed_visits.append(about_visit_person)
    
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
