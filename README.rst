statsd panel for django-debug-toolbar
=====================================

This toolbar panel will display all statsd data that was sent while processing
the current request.


Getting started
---------------

 * Install the statsd_toolbar package::
    
    python setup.py install


 * Add the panel to DEBUG_TOOLBAR_PANELS::

    DEBUG_TOOLBAR_PANELS = (
        'statsd_toolbar.panels.StatsDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
        ...
    )

* Add statsd_toolbar to INSTALLED_APPS::
    
    INSTALLED_APPS = (
        ...
        'statsd_toolbar',
        ...
    )
