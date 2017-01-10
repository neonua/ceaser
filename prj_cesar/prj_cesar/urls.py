from django.conf.urls import url
from cesar_app.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index, name='index')
]
