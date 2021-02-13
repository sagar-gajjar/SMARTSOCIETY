from django.shortcuts import render
from .models import *
from chairman.models import *

# Create your views here.

def registration(request):
    return render(request,"watchman/registration.html")

def register_watchman(request):
    name=request.POST['name']
    email=request.POST['email']
    contact_no=request.POST['contact_no']

    wid=Watchman.objects.create(firstname=name,email=email,contact_no=contact_no)
    return render(request,"watchman/registration.html")

def w_login(request):
    return render(request,"watchman/w_login.html")
    
def w_login_evalute(request):
    try:
        w_email=request.POST['email']
        w_password=request.POST['password']
        sid=Watchman.objects.get(email=w_email)
        if sid:
            if sid.password==w_password:
                request.session['w_email']=sid.email
                request.session['w_firstname']=sid.firstname
                return render(request,"watchman/w_index.html",{'sid':sid})
            else:
                e_msg="Invalid Email or Password"
                return render(request,"watchman/w_login.html",{'e_msg':e_msg})
    except:
        e_msg="Invalid Email or Password"
        return render(request,"watchman/w_login.html",{'e_msg':e_msg})

def w_logout(request):
    if "w_email" in request.session:
        del request.session['w_email']
        del request.session['w_firstname']
        return render(request,"watchman/w_login.html")
    else:
        return render(request,"watchman/w_login.html")

def w_index(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        return render(request,"watchman/w_index.html",{'sid':sid})
    else:
        return render(request,"watchman/w_login.html")

def watchman_profile(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        return render(request,"watchman/watchman_profile.html",{'sid':sid})
    else:
        return render(request,"watchman/w_login.html")

def watchman_update_profile(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        if "pic" not in request.FILES:
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            password=request.POST['password']
            blood_group=request.POST['blood_group']
            family_contact_no=request.POST['family_contact_no']
            contact_no=request.POST['contact_no']
            address=request.POST['address']
            age=request.POST['age']
        else:
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            password=request.POST['password']
            blood_group=request.POST['blood_group']
            family_contact_no=request.POST['family_contact_no']
            contact_no=request.POST['contact_no']
            address=request.POST['address']
            pic=request.FILES['pic']
            age=request.POST['age']
            sid.profile_picture=pic

        sid.firstname=firstname
        sid.lastname=lastname
        sid.password=password
        sid.blood_group=blood_group
        sid.family_contact_no=family_contact_no
        sid.contact_no=contact_no
        sid.address=address
        sid.age=age
        sid.save()
        return render(request,"watchman/watchman_profile.html",{'sid':sid})
    else:
        return render(request,"watchman/w_login.html")

def w_allmember(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        data=Member.objects.all()
        return render(request,"watchman/w_allmember.html",{'sid':sid,'data':data})
    else:
        return render(request,"watchman/w_login.html")

def w_view_member(request,pk):
    if "w_email" in request.session:
        user=Member.objects.get(id=pk)
        sid=Watchman.objects.get(email=request.session['w_email'])
        return render(request,"watchman/w_view_member.html",{'sid':sid,'user':user})
    else:        
        return render(request,"watchman/w_login.html")

def w_notice_view(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        data=Notice.objects.all()
        return render(request,"watchman/w_notice_view.html",{'sid':sid,'data':data})
    else:
        return render(request,"watchman/w_login.html")

def w_gallary(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        data=Gallary.objects.all()
        return render(request,"watchman/w_image-gallery.html",{'sid':sid,'data':data})
    else:
        return render(request,"watchman/w_login.html")

def w_v_gallary(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        data=VideoGallary.objects.all()
        return render(request,"watchman/w_video_view.html",{'sid':sid,'data':data})
    else:
        return render(request,"watchman/w_login.html")

def w_visitors_list(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        return render(request,"watchman/w_visitors_list.html",{'sid':sid})
    else:
        return render(request,"watchman/w_login.html")

def w_all_contact(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        data=Member.objects.exclude(email=request.session['s_email'])
        return render(request,"watchman/w_all_contact.html",{'sid':sid,'data':data})
    else:
        return render(request,"watchman/w_login.html")

def w_e_contact(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        return render(request,"watchman/w_emergency.html",{'sid':sid})
    else:
        return render(request,"watchman/w_login.html")

def w_events(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        data=Event.objects.all()
        return render(request,"watchman/w_event_list.html",{'sid':sid,'data':data})
    else:
        return render(request,"watchman/w_login.html")

def w_visitors(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        return render(request,"watchman/add_visitors.html",{'sid':sid})
    else:
        return render(request,"watchman/w_login.html")

def w_add_visitors(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        contact_no=request.POST['contact_no']
        address=request.POST['address']
        Visitor.objects.create(firstname=firstname,lastname=lastname,contact_no=contact_no,address=address)
        return render(request,"watchman/add_visitors.html",{'sid':sid})
    else:
        return render(request,"watchman/w_login.html")

def w_visitors_list(request):
    if "w_email" in request.session:
        sid=Watchman.objects.get(email=request.session['w_email'])
        data=Visitor.objects.all()
        return render(request,"watchman/w_visitors_list.html",{'sid':sid,'data':data})
    else:
        return render(request,"watchman/w_login.html")
