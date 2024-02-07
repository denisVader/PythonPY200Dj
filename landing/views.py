from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import MyForm
from django.http import JsonResponse

class MyTemplateViev(TemplateView):
    template_name = "landing/index.html"

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')
            data = form.cleaned_data
            data["ip"] = ip
            data["user_agent"] = user_agent
            return JsonResponse(data, json_dumps_params={'indent': 4,
                                                         'ensure_ascii': False})
        self.get(request)
# Create your views here.
