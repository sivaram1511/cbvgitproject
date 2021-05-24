from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
# Create your views here.
class Helloworldview(View):
    def get(self,request):
        return HttpResponse("<h1> this is class bassed view</h1>")
class Welcomeview(View):
    def get(self,request):
        return HttpResponse("<h1>this is welcome msg from class based views</h1>")
class HelloTemplate(TemplateView):
    template_name='testapp/result.html'
class TemplateContext(TemplateView):
    template_name="testapp/info.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']="siva"
        context['subject']="python"
        context['marks']=100
        return context


