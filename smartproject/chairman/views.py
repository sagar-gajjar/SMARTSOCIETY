from django.shortcuts import render
from .models import *
from watchman.models import *
import random
from .utils import sendmail

# Create your views here.

def index(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        m_count=Member.objects.all().count()
        n_count=Notice.objects.all().count()
        e_count=Event.objects.all().count()
        amd=Member.objects.filter().order_by('-id')[:3]
        el=Event.objects.filter().order_by('-id')[:1]
        nv=Notice.objects.filter().order_by('-id')[:1]
        return render(request,"chairman/dashboard/index.html",{'nv':nv,'amd':amd,'uid':uid,'m_count':m_count,'n_count':n_count,'e_count':e_count,'el':el})
    else:
        return render(request,"chairman/dashboard/login.html")

def login(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        m_count=Member.objects.all().count()
        n_count=Notice.objects.all().count()
        e_count=Gallary.objects.all().count()
        dt=Member.objects.all()
        return render(request,"chairman/dashboard/index.html",{'uid':uid,'m_count':m_count,'n_count':n_count,'e_count':e_count,'dt':dt})
    else:
        return render(request,"chairman/dashboard/login.html")

def login_evalute(request):
    try:
        u_email=request.POST['email']
        u_password=request.POST['password']
        uid=Chairman.objects.get(email=u_email)
        if uid:
            if uid.password==u_password:
                request.session['c_email']=uid.email
                request.session['c_firstname']=uid.firstname
                m_count=Member.objects.all().count()
                n_count=Notice.objects.all().count()
                e_count=Event.objects.all().count()
                amd=Member.objects.filter().order_by('-id')[:3]
                el=Event.objects.filter().order_by('-id')[:1]
                nv=Notice.objects.filter().order_by('-id')[:1]
                return render(request,"chairman/dashboard/index.html",{'nv':nv,'amd':amd,'uid':uid,'m_count':m_count,'n_count':n_count,'e_count':e_count,'el':el})
            else:
                e_msg="Invalid Email or Password"
                return render(request,"chairman/dashboard/login.html",{'e_msg':e_msg})
    except:
        e_msg="Invalid Email or Password"
        return render(request,"chairman/dashboard/login.html",{'e_msg':e_msg})

def logout(request):
    if "c_email" in request.session:
        del request.session['c_email']
        del request.session['c_firstname']
        return render(request,"chairman/dashboard/login.html")
    else:
        return render(request,"chairman/dashboard/login.html")

def chairman_profile(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        return render(request,"chairman/dashboard/chairman_profile.html",{'uid':uid})
    else:
        return render(request,"chairman/dashboard/login.html")

def chairman_update_profile(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
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

        uid.firstname=firstname
        uid.lastname=lastname
        uid.password=password
        mid=MemberDetails.objects.get(house_no=uid.m_id)
        mid.house_no=house_no
        mid.job_profession=job_profession
        mid.job_address=job_address
        mid.vehicle_type=vehicle_type
        mid.vehicle_details=vehicle_details
        mid.blood_group=blood_group
        mid.family_member_details=family_member_details
        mid.contact_no=contact_no
        mid.address=address
        uid.save()
        mid.save()
        return render(request,"chairman/dashboard/chairman_profile.html",{'uid':uid})

def add_member(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        return render(request,"chairman/dashboard/add_member.html",{'uid':uid})
    else:        
        return render(request,"chairman/dashboard/login.html")

def register_member(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        member_role="society member"
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        house_no=request.POST['house_no']
        address=request.POST['address']
        job_profession=request.POST['job_profession']
        job_address=request.POST['job_address']
        vehicle_type=request.POST['vehicle_type']
        vehicle_details=request.POST['vehicle_details']
        blood_group=request.POST['blood_group']
        family_member_details=request.POST['family_member_details']
        contact_no=request.POST['contact_no']
        password=firstname[:3]+lastname[-3:]+str(random.randint(111,999))+contact_no[-3:]
        
        mid=MemberDetails.objects.create(member_role=member_role,house_no=house_no,address=address,job_profession=job_profession
        ,job_address=job_address,vehicle_type=vehicle_type,vehicle_details=vehicle_details,blood_group=blood_group
        ,family_member_details=family_member_details,contact_no=contact_no)
        
        member_id=Member.objects.create(m_id=mid,firstname=firstname,lastname=lastname,email=email,password=password)
        
        sendmail("Confirmation mail","mail_template",email,{'password':password,'member_id':member_id})

        return render(request,"chairman/dashboard/index.html",{'uid':uid})
    else:        
        return render(request,"chairman/dashboard/login.html")

def all_members(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        data=Member.objects.all()
        return render(request,"chairman/dashboard/all_members.html",{'data':data,'uid':uid})
    else:        
        return render(request,"chairman/dashboard/login.html")

def edit_member_details(request,pk):
    if "c_email" in request.session:
        user=Member.objects.get(id=pk)
        uid=Chairman.objects.get(email=request.session['c_email'])
        return render(request,"chairman/dashboard/edit_member_details.html",{'uid':uid,'user':user})
    else:        
        return render(request,"chairman/dashboard/login.html")

def update_member_details(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        member_role="society_member"
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        house_no=request.POST['house_no']
        address=request.POST['address']
        job_profession=request.POST['job_profession']
        job_address=request.POST['job_address']
        vehicle_type=request.POST['vehicle_type']
        vehicle_details=request.POST['vehicle_details']
        blood_group=request.POST['blood_group']
        family_member_details=request.POST['family_member_details']
        contact_no=request.POST['contact_no']
        
        user=Member.objects.get(email=email)
        mid=MemberDetails.objects.get(house_no=user.m_id)
        
        mid.house_no=house_no
        mid.address=address
        mid.job_profession=job_profession
        mid.job_address=job_address
        mid.vehicle_type=vehicle_type
        mid.vehicle_details=vehicle_details
        mid.blood_group=blood_group
        mid.family_member_details=family_member_details
        mid.contact_no=contact_no
        user.firstname=firstname
        user.lastname=lastname

        user.save()
        mid.save()
        
        return render(request,"chairman/dashboard/edit_member_details.html",{'uid':uid,'user':user})
    else:        
        return render(request,"chairman/dashboard/login.html")

def delete_member(request,pk):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        user=Member.objects.get(id=pk)
        
        mid=MemberDetails.objects.get(house_no=user.m_id)

        mid.delete()
        user.delete()
        
        data=Member.objects.all()
        return render(request,"chairman/dashboard/all_members.html",{'uid':uid,'data':data})
    else:        
        return render(request,"chairman/dashboard/login.html")

def view_member_details(request,pk):
    if "c_email" in request.session:
        user=Member.objects.get(id=pk)
        uid=Chairman.objects.get(email=request.session['c_email'])
        
        return render(request,"chairman/dashboard/view_member_profile.html",{'uid':uid,'user':user})
    else:        
        return render(request,"chairman/dashboard/login.html")

def view_member(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        return render(request,"chairman/dashboard/view_member_profile.html",{'uid':uid,'user':user})
    else:        
        return render(request,"chairman/dashboard/login.html")

def visitors_list(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        data=Visitor.objects.all()
        return render(request,"chairman/dashboard/visitors_list.html",{'uid':uid,'data':data})
    else:        
        return render(request,"chairman/dashboard/login.html")

def notice_board(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        return render(request,"chairman/dashboard/notice_board.html",{'uid':uid})
    else:        
        return render(request,"chairman/dashboard/login.html")

def notice_sub(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        notice_sub=request.POST['notice_sub']
        about_notice=request.POST['about_notice']
        Notice.objects.create(notice_sub=notice_sub,about_notice=about_notice)
        return render(request,"chairman/dashboard/notice_board.html",{'uid':uid})
    else:        
        return render(request,"chairman/dashboard/login.html")

def notice_view(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        data=Notice.objects.all()
        return render(request,"chairman/dashboard/notice_board_view.html",{'uid':uid,'data':data})
    else:        
        return render(request,"chairman/dashboard/login.html")

def add_pictures_page(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        return render(request,"chairman/dashboard/add_pictures_page.html",{'uid':uid})
    else:
        return render(request,"chairman/dashboard/login.html")

def add_pictures(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        if "pic" in request.FILES:
            name=request.POST['picname']
            pic=request.FILES['pic']
            picid=Gallary.objects.create(name=name,pic=pic)
            data=Gallary.objects.all()
            return render(request,"chairman/dashboard/image-gallery.html",{'uid':uid,'data':data})
        else:
            data=Gallary.objects.all()

            return render(request,"chairman/dashboard/image-gallery.html",{'uid':uid,'data':data})
    else:
        return render(request,"chairman/dashboard/login.html")

def pictures(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        data=Gallary.objects.all()
        return render(request,"chairman/dashboard/image-gallery.html",{'uid':uid,'data':data})
    else:
        return render(request,"chairman/dashboard/login.html")

def add_video(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        return render(request,"chairman/dashboard/add_video_page.html",{'uid':uid})
    else:
        return render(request,"chairman/dashboard/login.html")

def upload_video(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        videoname=request.POST['videoname']
        clip=request.FILES['clip']
        vid=VideoGallary.objects.create(name=videoname,videofile=clip)
        data=VideoGallary.objects.all()
        return render(request,"chairman/dashboard/video_view.html",{'uid':uid,'data':data})
    else:
        return render(request,"chairman/dashboard/login.html")

def videos(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        data=VideoGallary.objects.all()
        return render(request,"chairman/dashboard/video_view.html",{'uid':uid,'data':data})
    else:
        return render(request,"chairman/dashboard/login.html")

def c_forgot_password(request):
    return render(request,"chairman/dashboard/c_forgot-password.html")

def e_forgot_password(request):
    try:
        u_email=request.POST['email']
        uid=Chairman.objects.get(email=u_email)
        if uid:
            otp=str(random.randint(000000,999999))
            sendmail("Confirmation Mail","otp_mail",u_email,{"otp":otp})
            return render(request,"chairman/dashboard/otp_forgot-password.html",{'uid':uid,'otp':otp})
    except:
        e_msg="Invalid Email...."
        return render(request,"chairman/dashboard/c_forgot-password.html",{'e_msg':e_msg})

def otp_forgot_password(request):
    try:
        u_email=request.POST['email']
        sent_otp=request.POST['sent_otp']
        u_otp=request.POST['otp']
        if sent_otp==u_otp:
            return render(request,"chairman/dashboard/forgot_password.html",{'email':u_email})
        else:
            e_msg="Invalid OTP...."
            return render(request,"chairman/dashboard/c_forgot-password.html",{'e_msg':e_msg})
    except:
        e_msg="Invalid OTP...."
        return render(request,"chairman/dashboard/c_forgot-password.html",{'e_msg':e_msg})

def forgot_password(request):
    try:
        u_email=request.POST['email']
        new_password=request.POST['new_password']
        retype_password=request.POST['retype_password']
        if new_password==retype_password:
            uid=Chairman.objects.get(email=u_email)
            uid.password=new_password
            uid.save()
            return render(request,"chairman/dashboard/index.html",{'uid':uid})
        else:
            e_msg="Both Password are not match...."
            return render(request,"chairman/dashboard/forgot_password.html",{'e_msg':e_msg})
    except:
        e_msg="Both Password are not match...."
        return render(request,"chairman/dashboard/forgot_password.html",{'e_msg':e_msg})

def delete_picture(request,pk):
    if "c_email" in request.session:
        gid=Gallary.objects.get(id=pk)
        uid=Chairman.objects.get(email=request.session['c_email'])
        gid.delete()
        data=Gallary.objects.all()
        return render(request,"chairman/dashboard/image-gallery.html",{'uid':uid,'data':data})
    else:
        return render(request,"chairman/dashboard/login.html")

def all_contact(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        data=Member.objects.all()
        return render(request,"chairman/dashboard/all_contact.html",{'uid':uid,'data':data})
    else:
        return render(request,"chairman/dashboard/login.html")

def e_contact(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        return render(request,"chairman/dashboard/emergency.html",{'uid':uid})
    else:
        return render(request,"chairman/dashboard/login.html")

def add_event_page(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        return render(request,"chairman/dashboard/add_event.html",{'uid':uid})
    else:
        return render(request,"chairman/dashboard/login.html")

def add_event(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        event_sub=request.POST['event_subject']
        event_description=request.POST['event_description']
        event_date=request.POST['event_date']
        event_time=request.POST['event_time']
        event_pic=request.FILES['event_pic']

        eid=Event.objects.create(event_subject=event_sub,event_description=event_description,event_date=event_date,event_time=event_time,event_picture=event_pic)
        
        return render(request,"chairman/dashboard/add_event.html",{'uid':uid})
    else:
        return render(request,"chairman/dashboard/login.html")

def view_event(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        data=Event.objects.all()
        return render(request,"chairman/dashboard/event_list.html",{'uid':uid,'data':data})
    else:
        return render(request,"chairman/dashboard/login.html")

def edit_event(request,pk):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        eid=Event.objects.get(id=pk)
        data=Event.objects.all()
        return render(request,"chairman/dashboard/edit_event.html",{'uid':uid,'eid':eid,'data':data})
    else:
        return render(request,"chairman/dashboard/login.html")

def edit_event_detail(request):
    pass

def all_watchman(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        data=Watchman.objects.all()
        return render(request,"chairman/dashboard/all_watchman.html",{'uid':uid,'data':data})
    else:
        return render(request,"chairman/dashboard/login.html")

def watchman_status(request,pk,status):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        w_id=Watchman.objects.get(id=pk)
        data=Watchman.objects.all()
        w_id.status=status
        if w_id.status=="Approved":
            password=w_id.firstname[:3]+str(random.randint(1111,9999))
            w_id.password=password
            sendmail("Confirmation Mail","watchman_mail",w_id.email,{"status":status,'password':password})
        w_id.save()
        return render(request,"chairman/dashboard/all_watchman.html",{'uid':uid,'data':data})
    else:
        return render(request,"chairman/dashboard/login.html")

def c_maintenance(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        return render(request,"chairman/dashboard/maintenance.html",{'uid':uid})
    else:        
        return render(request,"chairman/dashboard/login.html")

def add_maintenance(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        m_sub=request.POST['m_sub']
        m_des=request.POST['m_des']
        Maintenance.objects.create(m_sub=m_sub,m_des=m_des)
        return render(request,"chairman/dashboard/maintenance.html",{'uid':uid})
    else:        
        return render(request,"chairman/dashboard/login.html")

def view_maintenance(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        data=Maintenance.objects.all()
        return render(request,"chairman/dashboard/maintenance_view.html",{'uid':uid,'data':data})
    else:        
        return render(request,"chairman/dashboard/login.html")

def c_view_complaint(request):
    if "c_email" in request.session:
        uid=Chairman.objects.get(email=request.session['c_email'])
        data=Complaint.objects.all()
        return render(request,"chairman/dashboard/c_complaint_view.html",{'uid':uid,'data':data})
    else:        
        return render(request,"chairman/dashboard/login.html")

