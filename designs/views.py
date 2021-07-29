from django.shortcuts import render
from .models import Template


# Create your views here.
def templates(request):

	templates = Template.objects.all()

	context = {'templates': templates}



	return render(request, 'designs/templates.html', context)




def template_sample_preview(request, slug):

	template = Template.objects.get(slug=slug)

	name = template.name
	temp_name = 'designs/' + name + '.html'
	print(temp_name)

	context = {'templates': templates}


	return render(request, temp_name, context)