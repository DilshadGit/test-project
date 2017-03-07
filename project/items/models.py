from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify

# Create your models here.


def upload_image_location(instance, filename):
    return '%s/%s' % (instance.id, filename)


class Car(models.Model):
    # This line below will tell the browser who create the page
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    car_name = models.CharField(max_length=120, blank=False, null=True)
    car_model = models.CharField(max_length=7, blank=False, null=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_image_location, null=True,
                              blank=True, height_field="height_field", width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.car_name

    def get_absolute_url(self):
        return reverse('items:item_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-create_date', '-updated']


def create_slug(instance, new_slug=None):
    slug = slugify(instance.car_name)
    if new_slug is not None:
        slug = new_slug
    query_set = Car.objects.filter(slug=slug).order_by('-id')
    exists = query_set.exists()
    if exists:
        new_slug = '%s-%s' % (slug, query_set.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_item_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_item_receiver, sender=Car)
