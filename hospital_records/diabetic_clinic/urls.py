from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('search',views.search,name='search'),
	path('insertnew',views.insertnew,name='insertnew'),
	path('insertreports',views.insertreports,name='insertreports'),
	path('inserttreatment',views.inserttreatment,name='inserttreatment'),
	path('fetch_history',views.fetch_history,name='fetch_history'),
	path('fetch_report',views.fetch_report,name='fetch_report'),
	path('fetch_treatment',views.fetch_treatment,name='fetch_treatment'),
	path('advanced_search',views.advanced_search,name='advanced_search'),
]
