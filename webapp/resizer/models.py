from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

#Data fields model that is to be stored in the sqlite3 database
class Post(models.Model):

    #image_field= models.FileField(null=True, blank=True)

    image_field = models.ImageField()
    pub_date = models.DateTimeField( )

    # models.cascade deletes all the data associated with the deleted object
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    caption= models.CharField(max_length=250)



    def save(self):
        #Opening the uploaded image
        im = Image.open(self.image_field)

        output = BytesIO()

        #Resize/modify the image
        im = im.resize( (500,500) )

        #after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        #change the imagefield value to be the newley modifed image value
        self.image_field = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image_field.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)


        super(Post,self).save()
