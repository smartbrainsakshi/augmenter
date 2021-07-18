from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name='rl'
urlpatterns = [

    url(r'^index', views.my_form_post),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
