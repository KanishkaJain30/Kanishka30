from django.db import models
from django.conf import settings
from django.utils import timezone

class Tweet(models.Model):
    tweet_id=models.IntegerField(primary_key=True)
    tweet_text=models.CharField(max_length=500)
    tweet_url=models.URLField()
    user_id = models.BigIntegerField()
    user_handle_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=200)
       
    def __str__(self):
        return str(self.tweet_id) + ' == ' + self.user_name

class Domain(models.Model):
    
    # Create composite key of both the attributes
    class Meta:
        unique_together = (('tweet_id', 'domain_name'), )
    
    tweet_id = models.BigIntegerField()
    domain_name = models.URLField()

    def __str__(self):
        return str(self.tweet_id) + ' == ' + self.domain_name
# Create your models here.
