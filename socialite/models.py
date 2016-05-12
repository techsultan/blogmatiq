from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.text import slugify 
from django.contrib.auth.models import User 
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey 


# Create your models here.
class Socialite(models.Model):
	user = models.OneToOneField(User, related_name="socialite")
	profile_page = models.SlugField(max_length=120, blank=True)
	joined = models.DateTimeField(auto_now_add=True)
	bio = models.TextField(max_length=500)


class ContentTypeModel(models.Model):
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	class Meta:
		abstract = True 

class Tag(ContentTypeModel):
	tag = models.CharField(max_length=100)
	page = models.SlugField(max_length=120, blank=True)


	def save(self, *args, **kwargs):
		if not self.page:
			self.page = slugify(self.tag)
		super(Tag, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.tag 

class Comment(ContentTypeModel):
	title = models.CharField(max_length=100)
	commenter = models.ForeignKey(Socialite, related_name="comments")
	page = models.SlugField(max_length=120, blank=True)
	comment_date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if not self.page:
			self.page = slugify(self.title)
		super(Comment, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s" % (self.title)

