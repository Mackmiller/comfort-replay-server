from django.db import models
# from django.contrib.auth import get_user_model

# Create your models here.
class Show(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  key = models.CharField(max_length=100)
  value = models.IntegerField()
  class Meta:
        unique_together = ["key", "value"]

  def __str__(self):
    # This must return a string
    return f"The show named '{self.key}' has been watched {self.value} times."

  def as_dict(self):
    """Returns dictionary version of Show models"""
    return {
        'id': self.id,
        'key': self.key,
        'value': self.value
    }
