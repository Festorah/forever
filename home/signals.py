from django.db.models.signals import post_save
from django.dispatch import receiver
# from .models import WeddingProfileInfo
from django.template.defaultfilters import slugify


# @receiver(post_save, sender=WeddingProfileInfo)
# def update_weddingprofileinfo(sender, instance, created, **kwargs):
# 	if created:
# 		info = WeddingProfileInfo.objects.get(pk=instance.pk)
# 		slugname = info.user_first_name + ' and ' + info.user_partner_first_name + ' ' + str(info.id)
# 		info.slug = slugify(slugname)
# 		info.save()

