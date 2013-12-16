from django.conf.urls.defaults import *
from django.conf import settings
# from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Admin:
    (r'^admin/', include(admin.site.urls)),
    # Home:
    url(r'^', include('apps.home.urls', namespace="home_app")),
)

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL, 
#         document_root=settings.MEDIA_ROOT
#     )

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.STATIC_URL, 
#         document_root=settings.STATIC_ROOT
#     )