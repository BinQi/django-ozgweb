#coding:utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	
	#��̨
	url(r'^admin/index$', 'simple.views_admin.index'),
	url(r'^admin/admin$', 'simple.views_admin.admin'),
	
	#ǰ̨
	url(r'^site/index$', 'simple.views_site.index'),

)
