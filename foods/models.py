from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from restaurants.models import Restaurant


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'food_category'
        verbose_name_plural = 'food_categories'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'restaurants:foods_list_by_category',
            args=[self.slug]
        )

    @property
    def get_absolute_url_for_customer(self):
        return reverse(
            'foods:foods_list_by_category',
            args=[self.slug]
        )


class FoodTemplate(models.Model):
    category = models.ForeignKey(Category, related_name='foodtemplates', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='food/images', blank=True)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Food(models.Model):
    category = models.ForeignKey(Category, related_name='foods', on_delete=models.CASCADE)
    name = models.CharField(db_index=True, max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)
    image = models.ImageField(upload_to='food/images', blank=True)
    restaurant = models.ForeignKey(Restaurant, related_name='restaurant', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'restaurants:food_detail',
            args=[self.id]
        )
    
    @property
    def get_absolute_url_for_customer(self):
        return reverse(
            'foods:food_detail',
            args=[self.id]
        )