from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)

    def __str__(self):
        # return f'{self.first_name} {self.last_name}'
        return f'{self.id}'


class Statistic(models.Model):
    user_id = models.IntegerField()
    date = models.CharField(max_length=100)
    page_views = models.IntegerField()
    clicks = models.IntegerField()

    def __str__(self):
        return f'{self.user_id}'