from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView,CreateView
from django.http import HttpResponse
# Create your views here.
from testapp.models import Book


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
class Booklistview(ListView):
    model=Book
    #template_name = 'testapp/book.html'#our own template
    #context_object_name = 'list_of_book'#our own context name
class BookDetailview(DetailView):
    model=Book
    #default temlate name=book_detail.html
    #default context:book or object
class BookCreateview(CreateView):
    model=Book
    


