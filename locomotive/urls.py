from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from main.views import reload_view, drop_objects, page_view, on_submit

urlpatterns = [
    url(r'^$', page_view, name='main_page'),
    url(r'^admin/', admin.site.urls),
    url(r'^reload/', reload_view, name='reload'),
    url(r'^drop/', drop_objects, name='drop'),
    url(r'^submit/', on_submit, name='submit'),
]
