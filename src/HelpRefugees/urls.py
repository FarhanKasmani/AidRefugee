from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin

from searchFamily.views import FamilyListView, FamilyDetailView, addMember



from .views import home_page, people, updateLatLong, donate, guest
from accounts.views import login_page, register_page

urlpatterns = [
    url(r'^$', home_page),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_page, name='login'),
    url(r'^family/', include("searchFamily.urls", namespace='users')),
    url(r'^register/', register_page),
    url(r'^homepage/', home_page, name='home'),
    url(r'^people/', people, name='people'),
    url(r'^updateLatLong/', updateLatLong, name='updateLatLong'),
    url(r'^ngo/', include("ngo.urls", namespace='ngo')),
    url(r'^lost/', include("findLostPeople.urls", namespace='lost')),
    url(r'^guest/', guest, name="guest"),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
