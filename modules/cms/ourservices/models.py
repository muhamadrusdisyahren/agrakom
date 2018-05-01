from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class OurServices(models.Model):
    class Meta:
        db_table = 'our_services'

    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(blank=True)
    created_by = models.ForeignKey(User, blank=True, null=True, db_column='created_by', related_name='%(class)s_created_by')
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, db_column='modified_by', related_name='%(class)s_modified_by')
    modified_datetime = models.DateTimeField(auto_now=True, blank=True, null=True)


class OurServiceDetail(models.Model):
    class Meta:
        db_table = 'our_service_detail'

    Ourservices = models.ForeignKey(OurServices)
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='images/services')
    caption =  models.CharField(max_length=225,blank=True, null=True)
    status = models.BooleanField(blank=True)
    created_by = models.ForeignKey(User, blank=True, null=True, db_column='created_by', related_name='%(class)s_created_by')
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_by = models.ForeignKey(User, blank=True, null=True, db_column='modified_by', related_name='%(class)s_modified_by')
    modified_datetime = models.DateTimeField(auto_now=True, blank=True, null=True)
