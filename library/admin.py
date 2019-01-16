from django.contrib import admin
from .models import Book, Author,Image
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'date_of_birth')
	field = [
	'first_name', 'last_name', 'date_of_birth'
	]

admin.site.register(Author, AuthorAdmin)
class BookAdmin(admin.ModelAdmin):
	list_display = (
	'title', 'author', 'isbn', 'id', 'year_of_prod'
	)
	field = [
	'title', 'author', 'isbn', 'id', 'year_of_prod'
	]

admin.site.register(Book, BookAdmin)


admin.site.register(Image)