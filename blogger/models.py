from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.text import slugify 
from django.contrib.auth.models import User 


# Create your models here.
class Blogger(models.Model):
	user = models.OneToOneField(User, related_name="blogger")
	bio = models.TextField(max_length=500)
	page = models.SlugField(max_length=100, blank=True)
	joined = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(blank=True, null=True, editable=False)


	def __unicode__(self):
		return "%: %" % (self.user.username, self.joined)

	def save(self, *args, **kwargs):
		if not page:
			user_names = self.user.first_name + self.user.last_name
			self.page = slugify(user_names[:90])

		super(Blogger, self).save(*args, **kwargs)

class Blog(models.Model):
	blogger = models.ForeignKey(Blogger, related_name="blog")
	name = models.CharField(max_length=100)
	desc = models.TextField()
	page = models.SlugField(max_length=110, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(null=True, blank=True, editable=False)



class BlogCategory(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField(verbose_name="Description", max_length=350)
	page = models.SlugField(max_length=120, blank=True)
	blog = models.ForeignKey(Blog, related_name="categories")

	class Meta:
		verbose_name_plural = "Blog Categories"


	def __unicode__(self):
		return self.name 

class BlogPost(models.Model):
	category = models.ForeignKey(BlogCategory, related_name="posts")
	title = models.CharField(max_length=100)
	page = models.SlugField(max_length=120, blank=True)
	body = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(blank=True, null=True, editable=False)

	def __unicode__(self):
		return "%s => %s" % (self.title, self.category.name)
