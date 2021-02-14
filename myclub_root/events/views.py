from datetime import date
import calendar
from calendar import HTMLCalendar

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import EventSerializer
from .models import Event


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('event_date')
    serializer_class = EventSerializer


def index(request, year=date.today().year, month=date.today().month):
    t = date.today()
    # month = date.strftime(t, '%b')
    # year = t.year
    year = int(year)
    month = int(month)
    if year < 2000 or year > 2099:
        year = date.today().year
    month_name = calendar.month_name[month]

    cal = HTMLCalendar().formatmonth(year, month)

    title = "MyClub Event Calendar - %s %s" % (month_name, year)

    announcements = [
        {
            'date': '6-10-2020',
            'announcement': "Club Registrations Open"
        },
        {
            'date': '6-15-2020',
            'announcement': "Joe Smith Elected New Club President"
        }
    ]

    # return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
    return render(
        request,
        'events/index.html',
        {'title': title, 'cal': cal, "announcements": announcements}
    )


def all_events(request):
    events = Event.objects.all()

    return render(
        request,
        'events/events.html',
        {'title': "Event list", 'events': events}
    )
