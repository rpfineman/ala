#
# URLS (app)
#
from django.conf.urls import url
from . import views
#
from django_filters.views import FilterView
from feeds.filters import ChanFilter, RedditFilter, HackernewsFilter, SlashdotFilter

urlpatterns = [
    url( r'^$', views.index, name='index'),
    url( r'^c/$', views.ChanListView.as_view(), name='chan'),
    url( r'^r/$', views.RedditListView.as_view(), name='reddit'),
    url( r'^s/$', views.SlashdotListView.as_view(), name='slashdot'),
    url( r'^h/$', views.HackernewsListView.as_view(), name='hackernews'),
]

urlpatterns += [
    url(r'^c/search/$', FilterView.as_view(filterset_class=ChanFilter, template_name='feeds/chan_search_list.html'), name='chan-search'),
    url(r'^r/search/$', FilterView.as_view(filterset_class=RedditFilter, template_name='feeds/reddit_search_list.html'), name='reddit-search'),
    url(r'^s/search/$', FilterView.as_view(filterset_class=SlashdotFilter, template_name='feeds/slashdot_search_list.html'), name='slashdot-search'),
    url(r'^h/search/$', FilterView.as_view(filterset_class=HackernewsFilter, template_name='feeds/hackernews_search_list.html'), name='hackernews-search'),
]

urlpatterns += [
#    url(r'^r-detail/(?P<pk>\d+)$', views.RedditDetailView.as_view(), name='reddit-detail'),
    url(r'^c/(?P<pk>\d+)$', views.ChanDetailView.as_view(), name='chan-detail'),
    url(r'^r/(?P<pk>\d+)$', views.RedditDetailView.as_view(), name='reddit-detail'),
    url(r'^s/(?P<pk>\d+)$', views.SlashdotDetailView.as_view(), name='slashdot-detail'),
    url(r'^h/(?P<pk>\d+)$', views.HackernewsDetailView.as_view(), name='hackernews-detail'),
]

urlpatterns += [
    url(r'^c/(?P<pk>\d+)/update/$', views.chan_update, name='chan-update-form'),
    url(r'^c/(?P<pk>\d+)/update-star/$', views.chan_update_star, name='chan-update-star-form'),

    url(r'^r/(?P<pk>\d+)/update/$', views.reddit_update, name='reddit-update-form'),
    url(r'^r/(?P<pk>\d+)/update-star/$', views.reddit_update_star, name='reddit-update-star-form'),

    url(r'^s/(?P<pk>\d+)/update/$', views.slashdot_update, name='slashdot-update-form'),
    url(r'^s/(?P<pk>\d+)/update-star/$', views.slashdot_update_star, name='slashdot-update-star-form'),

    url(r'^h/(?P<pk>\d+)/update/$', views.hackernews_update, name='hackernews-update-form'),
    url(r'^h/(?P<pk>\d+)/update-star/$', views.hackernews_update_star, name='hackernews-update-star-form'),
]


urlpatterns += [
    url(r'^saved/$', views.saved, name='saved'),
]

