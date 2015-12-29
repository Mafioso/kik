from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from .api import persons, forms, requests
from . import views

admin.autodiscover()

router = DefaultRouter()
router.register(r'person', persons.PersonViewSet, 'person')
router.register(r'form', forms.FormViewSet, 'form')
router.register(r'request', requests.RequestViewSet, 'request')

urlpatterns = patterns('',
    url(r'^pkb/$', views.pkb_test),
    url(r'^gcvp/$', views.gcvp_test),
    url(r'^scoring/$', views.scoring_test),
    url(r'^documentolog/move/$', views.documentolog_move_test),
    url(r'^documentolog/edit/$', views.documentolog_edit_test),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
)
