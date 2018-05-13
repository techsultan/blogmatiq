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
	updated = models.DateTimeField(null=True, blank=True, editable=False)

	def save(self, *args, **kwargs):
		if not self.profile_page:
			user_names = self.user.first_name + self.user.last_name
			self.profile_page = slugify(self.user_names[:100])
		if self.joined:
			self.updated = timezone.now()
		super(Socialite, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.profile_page

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

class Comment(models.Model):
	commenter = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
	subject = models.CharField(max_length=100)
	link = models.SlugField(max_length=120, blank=True)
	blog_post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
	body = models.TextField(max_length=500)
	comment_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s" % (self.subject)

	def save(self, *args, **kwargs):
		if not self.link:
			self.link = slugify(self.subject)
		super(Comment, self).save(*args, **kwargs)


