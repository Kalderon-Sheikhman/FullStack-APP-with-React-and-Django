from django.db import models


class Certification(models.Model):
  certifications = models.CharField(max_length=300)
  author_name = models.CharField(max_length=100)
  author_title = models.CharField(max_length=100)
  author_photo = models.ImageField(upload_to='images')
  
  class Meta:
    verbose_name = 'Certification'
    verbose_name_plural = 'Certifications'
    
  def __str__(self):
    return self.author_name