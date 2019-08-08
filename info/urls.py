from django.urls import path

from . import views

app_name = 'info'
urlpatterns = [path('', views.index, name = 'index'),
		path('predict', views.predict, name = 'predict'),
		path('references', views.references, name = 'references'),
		path('predictions', views.predictions, name = 'predictions'),
		path('vocab', views.vocabulary, name = 'vocab')]