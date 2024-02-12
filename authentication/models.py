from django.db import models


# Create your models here.

class file_upload(models.Model):
    ids=models.AutoField(primary_key=True)
    file_name=models.CharField(max_length=255)
    my_file=models.FileField(upload_to='')

def __str__(self):
        return self.file_name  


class assignment(models.Model):
      
      full_name=models.CharField(max_length=30,null=True,default=None)

      date_field=models.DateField(auto_now=True)

      file_desc=models.CharField(max_length=255,null=True,default=None)

      file_name=models.CharField(max_length=55,null=True,)

      status=models.CharField(max_length=12,null=True,)

      myfiles=models.FileField(upload_to="")

      def __str__(self):
            return self.file_name







class myuploadjournels(models.Model):
      
      full_name=models.CharField(max_length=30,null=True,default=None)

      date_field=models.DateField(auto_now=True)

      file_desc=models.CharField(max_length=255,null=True,default=None)

      file_name=models.CharField(max_length=55,null=True,)

      status=models.CharField(max_length=12,null=True,)

      myfiles=models.FileField(upload_to="")

      def __str__(self):
            return self.file_name
      



class myuploadfees(models.Model):
      roll_no=models.AutoField(primary_key=True)
      first_name=models.CharField(max_length=20,null=True,default=None)
      f_desc=models.CharField(max_length=255,null=True,default=None)
      f_name=models.CharField(max_length=255,null=True,default=None)
      myfiles=models.FileField(upload_to="")

      def __str__(self):
            return self.f_name




class myclassnote(models.Model):
      
      full_name=models.CharField(max_length=30,null=True,default=None)

      comments=models.CharField(max_length=30,null=True,default=None)

      date_field=models.DateField(auto_now=True)

      file_desc=models.CharField(max_length=255,null=True,default=None)

      file_name=models.CharField(max_length=55,null=True,)

      status=models.CharField(max_length=12,null=True,)

      myfiles=models.FileField(upload_to="")

      def __str__(self):
            return self.file_name