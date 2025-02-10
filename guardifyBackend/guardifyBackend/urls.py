from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactCreate/', include('contact.urls')),
]

urlpatterns += [
    re_path(r'^(?!admin|api).*$', TemplateView.as_view(template_name='index.html'), name='index'),
]