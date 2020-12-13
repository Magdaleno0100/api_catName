from django.db import models


class Cat(models.Model):
    cat_name = models.CharField(max_length=20)
    cat_years = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.cat_name
