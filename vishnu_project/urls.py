from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'vishnu_project.views.index', name='index'),
    url(r'^$', include('numero.urls', namespace='numero', app_name='numero')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

]
