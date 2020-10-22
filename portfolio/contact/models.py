from django.db import models

class Contact(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  subject = models.CharField(max_length=250)
  message = models.TextField()
  sent_time = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-sent_time',)

  def __str__(self):
    return self.name
    