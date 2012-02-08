from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    '',
    url(r'^/$',
        'inventory_tracker.views.index',
    url(r'^inventories/(?P<inventory_id>\d+)$/',
        'inventory_tracker.views.inventory_detail')))
