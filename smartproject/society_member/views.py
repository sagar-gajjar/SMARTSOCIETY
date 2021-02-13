from django.shortcuts import render
from chairman.models import *
from watchman.models import *
import random
from .utils import sendmail

# Create your views here.

def s_login(request):
    if "s_email" in request.session:
            mid=Member.objects.get(email=request.session['s_email'])
            return render(request,"member/s_member.html",{'mid':mid})
    else:
        return render(request,"member/s_login.html")

def s_login_evalute(request):
    try:
        if "s_email" in request.session:
            mid=Member.objects.get(email=request.session['s_email'])
            return render(request,"member/s_member.html",{'mid':mid})
        else:
            s_email=request.POST['email']
            s_password=request.POST['password']
            mid=Member.objects.get(email=s_email)
            if mid:
                if mid.password==s_password and mid.status=="PENDING":
                    return render(request,"member/s_change_password.html",{'email':s_email})
                elif mid.password==s_password and mid.status=="ACTIVE":
                    request.session['s_id']=mid.id
                    request.session['s_email']=mid.email
                    return render(request,"member/s_member.html",{'mid':mid})
    except:
        e_msg="Invalid Email or Password"
        return render(request,"member/s_login.html",{'e_msg':e_msg})

def s_login_cpassword(request):
    try:
        s_email=request.POST['email']
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        retypepassword=request.POST['retypepassword']

        mid=Member.objects.get(email=s_email)
        if mid.password==oldpassword and newpassword==retypepassword:
            mid.password=newpassword
            mid.status="ACTIVE"
            mid.save()
            request.session['s_id']=mid.id
            request.session['s_email']=mid.email
            return render(request,"member/s_member.html",{'mid':mid})
    except:
        e_msg="Invalid Password"
        return render(request,"member/s_login.html",{'e_msg':e_msg})

def s_logout(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        del request.session['s_id']
        del request.session['s_email']
        return render(request,"member/s_login.html")
    else:
        e_msg="Invalid Password"
        return render(request,"member/s_login.html")

def s_reset_password(request):
    return render(request,"member/s_reset_password.html")

def s_allmember(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        data=Member.objects.exclude(email=request.session['s_email'])
        return render(request,"member/s_allmember.html",{'data':data,'mid':mid})
    else:
        return render(request,"member/s_login.html")

def member_profile(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        return render(request,"member/member_profile.html",{'mid':mid})
    else:
        return render(request,"member/s_login.html")

def member_update_profile(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        if "pic" not in request.FILES:
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            password=request.POST['password']
            house_no=request.POST['house_no']
            job_profession=request.POST['job_profession']
            job_address=request.POST['job_address']
            vehicle_type=request.POST['vehicle_type']
            vehicle_details=request.POST['vehicle_details']
            blood_group=request.POST['blood_group']
            family_member_details=request.POST['family_member_details']
            contact_no=request.POST['contact_no']
            address=request.POST['address']
        else:
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            password=request.POST['password']
            house_no=request.POST['house_no']
            job_profession=request.POST['job_profession']
            job_address=request.POST['job_address']
            vehicle_type=request.POST['vehicle_type']
            vehicle_details=request.POST['vehicle_details']
            blood_group=request.POST['blood_group']
            family_member_details=request.POST['family_member_details']
            contact_no=request.POST['contact_no']
            address=request.POST['address']
            pic=request.FILES['pic']
            uid.profile_picture=pic

        mid.firstname=firstname
        mid.lastname=lastname
        mid.password=password
        mid=MemberDetails.objects.get(house_no=mid.m_id)
        mid.house_no=house_no
        mid.job_profession=job_profession
        mid.job_address=job_address
        mid.vehicle_type=vehicle_type
        mid.vehicle_details=vehicle_details
        mid.blood_group=blood_group
        mid.family_member_details=family_member_details
        mid.contact_no=contact_no
        mid.address=address
        mid.save()
        return render(request,"member/member_profile.html",{'mid':mid})
    else:
        return render(request,"member/s_login.html")

def s_notice_view(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        data=Notice.objects.all()
        return render(request,"member/notice_view.html",{'mid':mid,'data':data})
    else:        
        return render(request,"member/s_login.html")

def s_gallary(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        data=Gallary.objects.all()
        return render(request,"member/s_image-gallery.html",{'mid':mid,'data':data})
    else:
        return render(request,"member/s_login.html")

def s_v_gallary(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        data=VideoGallary.objects.all()
        return render(request,"member/s_video_view.html",{'mid':mid,'data':data})
    else:
        return render(request,"member/s_login.html")

def s_visitors_list(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        data=Visitor.objects.all()
        return render(request,"member/s_visitors_list.html",{'mid':mid,'data':data})
    else:        
        return render(request,"member/s_login.html")

def s_all_contact(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        data=Member.objects.exclude(email=request.session['s_email'])
        return render(request,"member/s_all_contact.html",{'mid':mid,'data':data})
    else:        
        return render(request,"member/s_login.html")

def s_e_contact(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        return render(request,"member/s_emergency.html",{'mid':mid})
    else:        
        return render(request,"member/s_login.html")

def events(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        data=Event.objects.all()
        return render(request,"member/s_event_list.html",{'mid':mid,'data':data})
    else:        
        return render(request,"member/s_login.html")

def maintenance(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        data=Maintenance.objects.all()
        return render(request,"member/s_maintenance_view.html",{'mid':mid,'data':data})
    else:        
        return render(request,"member/s_login.html")

def complaint(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        return render(request,"member/complaint.html",{'mid':mid})
    else:        
        return render(request,"member/s_login.html")

def add_complaint(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        c_sub=request.POST['c_sub']
        c_des=request.POST['c_des']
        Complaint.objects.create(c_sub=c_sub,c_des=c_des)
        return render(request,"member/complaint.html",{'mid':mid})
    else:        
        return render(request,"member/s_login.html")

def view_complaint(request):
    if "s_email" in request.session:
        mid=Member.objects.get(email=request.session['s_email'])
        data=Complaint.objects.all()
        return render(request,"member/complaint_view.html",{'mid':mid,'data':data})
    else:        
        return render(request,"member/s_login.html")

