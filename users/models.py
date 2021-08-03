from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.template.defaultfilters import slugify
from designs.models import Template



class MyWebsite(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	bride_name = models.CharField(default="bride's name", max_length=100, blank=True, null=True)
	groom_name = models.CharField(default="groom's name", max_length=100, blank=True, null=True)
	wedding_date = models.DateField(blank=True, null=True)
	location = models.CharField(max_length=225, blank=True, null=True)
	bride_image = models.ImageField(default='bride_image.jpg', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
	groom_image = models.ImageField(default='groom_image.jpg', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
	about_bride = models.CharField(max_length=100, blank=True, null=True)
	about_groom = models.CharField(max_length=100, blank=True, null=True)

	hero_image_1 = models.ImageField(default='hero_image_1.jpg', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
	hero_image_2 = models.ImageField(default='hero_image_2.jpg', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
	hero_image_3 = models.ImageField(default='hero_image_3.jpg', upload_to='photos/%Y/%m/%d/', blank=True, null=True)

	how_we_met = models.TextField(default='How we met...', blank=True, null=True)
	first_outing = models.TextField(default='First_outing...', blank=True, null=True)
	proposal = models.TextField(default='Tell us about his proposal...', blank=True, null=True)
	courtship = models.TextField(default='Courtship...', blank=True, null=True)
	together_forever = models.TextField(default='Together Forever...', blank=True, null=True)

	gallery_1 = models.ImageField(default='gallery_1.jpg', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
	gallery_2 = models.ImageField(default='gallery_2.jpg', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
	gallery_3 = models.ImageField(default='gallery_3.jpg', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
	gallery_4 = models.ImageField(default='gallery_4.jpg', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
	gallery_5 = models.ImageField(default='gallery_5.jpg', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
	gallery_6 = models.ImageField(default='gallery_6.jpg', upload_to='photos/%Y/%m/%d/', blank=True, null=True)

	wedding_engagement_date = models.CharField(max_length=225, blank=True, null=True)
	wedding_engagement_time = models.CharField(max_length=225, blank=True, null=True)
	wedding_engagement_venue = models.CharField(max_length=225, blank=True, null=True)
	wedding_engagement_description = models.TextField(default='full description of the wedding engagement', blank=True, null=True)

	wedding_ceremony_time = models.CharField(max_length=225, blank=True, null=True)
	wedding_ceremony_venue = models.CharField(max_length=225, blank=True, null=True)
	wedding_ceremony_description = models.TextField(default='full description of the wedding ceremony...', blank=True, null=True)

	wedding_reception_time = models.CharField(max_length=15, blank=True, null=True)
	wedding_reception_venue = models.CharField(max_length=100, blank=True, null=True)
	wedding_reception_description = models.TextField(default='full description of the wedding reception...', blank=True, null=True)
	slug = models.SlugField(null=False) 
	registry = models.BooleanField(default=False, null=True)
	web_design_template = models.OneToOneField(Template, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.user)

	def save(self, *args, **kwargs):
		if not self.slug:
			slugname = self.bride_name + ' and ' + self.groom_name
			self.slug = slugify(slugname)
		return super().save(*args, **kwargs)
	
	
	@property
	def bride_imageURL(self):
		try:
			url = self.bride_image.url
		except:
			url=''
		return url
	@property
	def groom_imageURL(self):
		try:
			url = self.groom_image.url
		except:
			url=''
		return url



class GuestList(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=100, blank=True)
	number_of_guest= models.IntegerField()
	attending = models.CharField(max_length=100, blank=True)
	message = models.TextField()

	def __str__(self):
		return str(self.name)

class Comments(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=100, blank=True)
	date = models.DateTimeField(default=timezone.now)
	message = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.name)
