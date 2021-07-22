from django.shortcuts import render

posts = [
	{
		'author': 'Funso',
		'title': 'Blog Post 1',
		'date_posted': 'December 13, 2020',
		'content':'This is the first post content'
	},
	{
		'author': 'Festorah',
		'title': 'Blog Post 2',
		'date_posted': 'December 14, 2020',
		'content':'This is the second post content'
	}
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})

def port_folio(request):
	return render(request, 'blog/port_folio.html')

def invite(request):
	return render(request, 'blog/invite.html')
