from django.urls import path
from . import views
from ZomatoFood.views import (
		cities,search_Page,
		Cusion_search,
		collection_List,
		SearchHotelsInCity
	)
from django.conf.urls import url
urlpatterns = [
    url(r'^categories/', collection_List, name='Categories'),
    url(r'^cities/', SearchHotelsInCity, name='Cities'),
    url(r'$', search_Page),
]