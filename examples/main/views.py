from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from time import sleep
import statsd


def demo_one(request):
    # Do some statsd stuff, then render a template
    timer = statsd.Timer(__name__)
    counter = statsd.Counter(__name__)
    counter += 10
    timer.start()
    timer.stop('total')

    users = User.objects.all()
    context = RequestContext(request,
        {'foo': 'bar',
         'users': users}
    )
    return render_to_response('demo_one.html', context)

