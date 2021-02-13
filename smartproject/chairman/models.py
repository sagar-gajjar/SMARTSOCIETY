from django.db import models
from django.utils import timezone
import math

# Create your models here.

class MemberDetails(models.Model):
    member_role=models.CharField(max_length=30,blank=True) # Owner Rental Chairman
    house_no=models.CharField(max_length=30,blank=True)
    address=models.CharField(max_length=100,blank=True)
    job_profession=models.CharField(max_length=30,blank=True)
    job_address=models.CharField(max_length=100,blank=True)
    vehicle_type=models.CharField(max_length=30,blank=True)
    vehicle_details=models.CharField(max_length=100,blank=True)
    blood_group=models.CharField(max_length=30,blank=True)
    family_member_details=models.CharField(max_length=100,blank=True)
    contact_no=models.CharField(max_length=30,default="00")

    def __str__(self):
        return self.house_no

class Chairman(models.Model):
    m_id=models.ForeignKey(MemberDetails, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30,blank=True)
    lastname=models.CharField(max_length=30,blank=True)
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    profile_picture=models.FileField(upload_to='images/',default="default.jpg")

    def __str__(self):
        return self.firstname

class Member(models.Model):
    m_id=models.ForeignKey(MemberDetails, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30,blank=True)
    lastname=models.CharField(max_length=30,blank=True)
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    profile_picture=models.FileField(upload_to='images/',default="default.jpg")
    status=models.CharField(max_length=30,default="PENDING")

    def __str__(self):
        return self.firstname

class Notice(models.Model):
    notice_sub=models.CharField(max_length=100,blank=True)
    about_notice=models.CharField(max_length=999,blank=True)
    date=models.DateTimeField(auto_now_add=True,blank=False)
    u_date=models.DateTimeField(auto_now_add=True,blank=False)

    def __str__(self):
        return self.notice_sub

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"


class Gallary(models.Model):
    name=models.CharField(max_length=30,blank=True)
    pic=models.FileField(upload_to='images/',default="default.jpg")
    created_at=models.DateTimeField(blank=False,default=timezone.now)
    updated_at=models.DateTimeField(blank=False,default=timezone.now)

    def __str__(self):
        return self.name

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"


class VideoGallary(models.Model):
    name=models.CharField(max_length=30,blank=True)
    videofile=models.FileField(upload_to='videos/',null=True,verbose_name="video file")
    created_at=models.DateTimeField(blank=False,default=timezone.now)
    updated_at=models.DateTimeField(blank=False,default=timezone.now)

    def __str__(self):
        return self.name

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"

class Event(models.Model):
    event_subject=models.CharField(max_length=30,blank=True)
    event_description=models.CharField(max_length=100,blank=True)
    event_picture=models.FileField(upload_to='images/',default="defaultpic.png")
    event_date=models.DateField(blank=True)
    event_time=models.TimeField(blank=True)
    created_date=models.DateTimeField(auto_now_add=True,blank=False)
    updated_date=models.DateTimeField(auto_now_add=True,blank=False)

    def __str__(self):
        return self.event_subject
    
    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.created_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"

class Maintenance(models.Model):
    m_sub=models.CharField(max_length=100,blank=True)
    m_des=models.CharField(max_length=999,blank=True)
    date=models.DateTimeField(auto_now_add=True,blank=False)
    u_date=models.DateTimeField(auto_now_add=True,blank=False)

    def __str__(self):
        return self.m_sub

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"

class Complaint(models.Model):
    c_sub=models.CharField(max_length=100,blank=True)
    c_des=models.CharField(max_length=999,blank=True)
    date=models.DateTimeField(auto_now_add=True,blank=False)
    u_date=models.DateTimeField(auto_now_add=True,blank=False)

    def __str__(self):
        return self.c_sub

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"

