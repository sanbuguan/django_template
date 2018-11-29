from django.db import models



class test(models.Model):
    fid = models.AutoField(primary_key=True)
    
    class Meta:
        db_table = 'XXXX'