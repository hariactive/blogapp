from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField('Student Name',max_length=20,blank=False,null=False)
    age = models.IntegerField('Student Age', null=False)
    address = models.TextField('Student Address', null=False)
    
    
    def __str__(self):    #to get the meaningful data in the shell  from database
        return 'Name : ' +self.name + ' Age: ' + str(self.age) + ' Address: ' + self.address    