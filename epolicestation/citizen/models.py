from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique= True)
    password = models.CharField(max_length = 20)
    otp = models.IntegerField(default = 459)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    role = models.CharField(max_length = 10)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)

    def __str__(self):
        return self.email
   

class citizen(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    profile_pic=models.FileField(upload_to='images/',default='default-pic.png')
    contact_no=models.CharField(max_length=100,default="000000")
    address = models.CharField(max_length= 500, blank= True)
    gender = models.CharField(max_length=10)
    dob = models.DateField(blank=True)
    
    def __str__(self):
        return self.firstname
        
class law(models.Model):
    law_title = models.CharField(max_length=500)
    law_summary = models.CharField(max_length=500)
    law_rules1 = models.CharField(max_length=200)
    law_rules2 = models.CharField(max_length=200)
    law_rules3 = models.CharField(max_length=200)
    law_rules4 = models.CharField(max_length=200)
    law_rules5 = models.CharField(max_length=200)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)
    law_icon = models.CharField(max_length= 500, blank= True)

    def __str__(self):
        return self.law_title
        
class crime_category(models.Model):
    crime_category_name= models.CharField(max_length=500)

    def __str__(self):
        return self.crime_category_name
    

class Sub_crime(models.Model):
    crime_id=models.ForeignKey(crime_category, on_delete = models.CASCADE)
    sub_category_name= models.CharField(max_length=100)
    
    def __str__(self):
        return self.sub_category_name

class complaint(models.Model):
    citizen_id=models.ForeignKey(citizen, on_delete = models.CASCADE)
    complaint_title=models.CharField(max_length=50)
    complaint_description=models.CharField(max_length=500)
    complaint_no=models.CharField(max_length=100)
    proof_img=models.FileField(upload_to='images/')
    proof_video=models.FileField(upload_to='videos/',null=True,verbose_name="video file")



      
  
