from django.db import models

# Create your models here.
class MemberTag(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="Member Email", blank=True)
    telegram = models.CharField(max_length=100)
    date_of_birth = models.DateField(verbose_name="Date of birth", auto_now=False, blank=False)
    tags = models.ManyToManyField(MemberTag, blank=True)

    def __str__(self):
        return self.name+self.lastname

class Club(models.Model):
    title= models.CharField(max_length=50)
    leader = models.ForeignKey(Member, on_delete=models.PROTECT, blank=False)
    member = models.ManyToManyField(Member, related_name='%(class)s_of_the_club')
    def __str__(self):
        return self.title
