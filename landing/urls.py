from django.urls import path
from django.views.generic import TemplateView
from .views import MyTemplateViev
urlpatterns = [
    # path('', TemplateView.as_view(template_name="landing/index.html")),
    path('', MyTemplateViev.as_view()),
]