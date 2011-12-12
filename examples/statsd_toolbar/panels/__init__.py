""" A django-debug-toolbar panel for displaying data logged to statsd.
"""

from django.conf import settings
from debug_toolbar.panels import DebugPanel
import statsd


def get_stats_info(func, panel):
    """ Intercepts data before it is sent to the statsd server, and stores it
        so that it can be displayed in the debug panel.
    """
    def wrapped(conn, data, sample_rate=None): 
        if not sample_rate:
            sample_rate = conn._sample_rate

        panel._store_data(data, sample_rate)
        return func(conn, data, sample_rate)
    wrapped.__doc__ = func.__doc__
    wrapped.__name__ = func.__name__
    return wrapped

class StatsdDebugPanel(DebugPanel):
    name = 'Statsd data'
    template = 'panels/statsd.html'
    has_content = True

    def __init__(self, *args, **kwargs):
        super(StatsdDebugPanel, self).__init__(*args, **kwargs)
        statsd.Connection.send = get_stats_info(statsd.Connection.send, self)
        self.data = []

    def nav_title(self):
        return 'Statsd'

    def url(self):
        return ''

    def title(self):
        return self.nav_title()

    def _store_data(self, data, sample_rate, **kwargs):
        for stat, value in data.iteritems():
            self.data.append({'statistic': stat,
                              'value': value,
                              'sample_rate': sample_rate})

    def process_response(self, request, response):
        """ Processes a list of data that has been sent to statsd.
        """
        print 'processing'
        print self.data
        print dir(self)
        self.record_stats({
            'data': self.data
        })
















