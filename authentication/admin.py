from django.contrib import admin

from .models import file_upload

from .models import assignment


from.models import myuploadjournels

from.models import myuploadfees


from.models import myclassnote
# from .models import Student


# Register your models here.0.  

admin.site.register(file_upload)

admin.site.register(assignment)

admin.site.register(myuploadjournels)

admin.site.register(myuploadfees)

admin.site.register(myclassnote)


 