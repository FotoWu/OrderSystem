from django.conf.urls import include, url
from django.contrib import admin
from Order import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^menu/', views.menu, name='menu'),
    url(r'^menu.html$', views.menu, name='get_tag'),
    url(r'^display_order/', views.display_order, name='display_order'),
    url(r'^add_order.html$', views.add_order, name='add_order'),
    url(r'^remove_order.html$', views.remove_order, name='remove_order'),
    url(r'^submit', views.submit, name='submit')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
