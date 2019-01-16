from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Book, Author, Image
from django.db.models import Q
from .forms import ContactForm


def index(request):
	return render(request, 'index.html')
def about(request):
	return render(request, 'about_us.html')
def contact(request):
	form = ContactForm()
	return render_to_response('contact_us.html', {'form':form})
def lfe(request):
	return render(request, 'LFE.html')
def ps(request):
	return render(request, 'ps.html')
def title(request):
	book = Book.objects.all()
	return render(request, 'title_list.html', {'book': book})
def title_detail(request, title_id):
	title = get_object_or_404(Book, pk=pk)
	return render(request, 'title_detail.html', { 'title': title })

def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
			Q(title__icontains=query),
			Q(author__first_name__icontains = query),
			Q(author__last_name__icontains=query))
		result = Book.objects.filter(qset).distinct()
	else:
		result =[]
	return render_to_response('search.html', {"result":result, "query":query})


class BookList(ListView):
	model = Book
	template_name = 'book_list.html'
	context_object_name = 'book_list'

class BookDetail(DetailView):
	model = Book
	template_name = 'book_detail.html'
	context_object_name = 'book_list'



class AuthorList(ListView):
	model = Author
	template_name = 'author_list.html'
	context_object_name = 'author_list'

class AuthorDetail(DetailView):
	model = Author
	template_name = 'author_detail.html'
	context_object_name = 'author_list'