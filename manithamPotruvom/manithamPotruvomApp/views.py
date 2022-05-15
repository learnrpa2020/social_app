from django.shortcuts import render
from .models import News,Post,Contact

# Create your views here.
def index(request):
	all_news=News.objects.all()
	news_dict={'News':all_news}
	return render(request,'index.html',news_dict)


def post(request):
	all_post=Post.objects.all()
	post_dict={'Posts':all_post}
	return render(request,'posts.html',post_dict)


def contact(request):
	all_contact=Contact.objects.all()
	contact_dict={'Contacts': all_contact}
	return render(request,'contact.html',contact_dict)
