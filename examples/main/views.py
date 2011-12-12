from django.shortcuts import render_to_response
from time import sleep
import statsd


def demo_one(request):
    # Do some statsd stuff, then render a template
    timer = statsd.Timer(__name__)
    counter = statsd.Counter(__name__)
    counter += 10
    timer.start()
    print 'testing'
    sleep(0.1)
    timer.stop('total')
    return render_to_response('demo_one.html')

