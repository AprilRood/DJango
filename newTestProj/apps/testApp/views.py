from django.shortcuts import render
from .models import Author, Book

# Create your views here.
def index(request):
	return render(request,"testApp/index.html")


def createAuthor(request):
	new_author = Author.objects.create(name=request.POST['name'])
	context = {
		"all_authors" : Author.objects.filter()

	}
	return render(request, "testApp/index.html", context)


def add(request):
	author = Author.objects.get(name = request.POST['author_name'])
	new_book = Book.objects.create(title=request.POST['title'])
	new_book.author.add(author)

	context = {
		"all_authors" : Author.objects.filter()

	}
	return render(request, "testApp/index.html", context)