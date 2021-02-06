from datetime import date

from django.shortcuts import render
from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar

from .models import Event


# Create your views here.

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

    # return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
    return render(
        request,
        'events/index.html',
        {'title': title, 'cal': cal}
    )


def all_events(request):
    events = Event.objects.all()

    return render(
        request,
        'events/events.html',
        {'title': "Event list", 'events': events}
    )
