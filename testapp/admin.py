from django.contrib import admin
from testapp.models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','pages','price']
admin.site.register(Book,BookAdmin)
# Register your models here.
