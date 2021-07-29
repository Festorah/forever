from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



# class WeddingProfileInfo(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
# 	user_first_name = models.CharField(max_length=100, blank=True)
# 	user_partner_first_name = models.CharField(max_length=100, blank=True)
# 	wedding_date = models.DateField(blank=True, null=True)
# 	location = models.CharField(max_length=225, blank=True)
# 	how_you_heard_about_us = models.CharField(max_length=100, blank=True) #To be properly sorted later on
# 	slug = models.SlugField(null=False) 
# 	date_registered = models.DateTimeField(default=timezone.now, blank=True, null=True)
# 	registry = models.BooleanField(default=False, null=True)

# 	def __str__(self):
# 		return str(self.user)

# 	def save(self, *args, **kwargs):
# 		if not self.slug:
# 			slugname = self.user_first_name + ' and ' + self.user_partner_first_name
# 			self.slug = slugify(slugname)
# 		return super().save(*args, **kwargs)