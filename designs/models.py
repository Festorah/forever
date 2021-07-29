from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Template(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	image = models.ImageField(upload_to='photos/designs/%Y/%m/%d/', blank=True, null=True)
	description = models.CharField(default='Tell us something about this design...', max_length=225, blank=True, null=True)
	slug = models.SlugField(null=False, unique=True)

	def __str__(self):
		return str(self.name)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)