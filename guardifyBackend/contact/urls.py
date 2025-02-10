'''from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import ContactCreateView

urlpatterns = [
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
]
'''

from django.urls import path
from .views import ContactCreateView

urlpatterns = [
    path('', ContactCreateView.as_view(), name='contact'),
]
