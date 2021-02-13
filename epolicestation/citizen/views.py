from django.shortcuts import render
from .models import *
from .utils import *
from random import randint

# Create your views here.
def index(request):
	if "c_email" in request.session:
		uid=User.objects.get(email=request.session['c_email'])
		cid=citizen.objects.get(user_id=uid)
		data=law.objects.all()
		
		context={
				'data':data,
				'uid':uid,
				'cid':cid,
		}
		return render(request,"citizen/index.html",{'context':context})
	else:
		data=law.objects.all()
		context={
				'data':data,
		}
		return render(request,"citizen/index.html",{'context':context})

def register_page(request):
	return render(request,"citizen/register.html")

def register_member(request):
	role="citizen"
	email=request.POST['email']
	firstname= request.POST['firstname']
	lastname= request.POST['lastname']
	address= request.POST['address']
	contact_no= request.POST['contact_no']
	password= request.POST['password']
	cpassword= request.POST['cpassword']
	gender= request.POST['gender']
	dob= request.POST['dob']
   	
	uid=User.objects.create(email=email,password=password,role=role)
	cid=citizen.objects.create(user_id=uid,firstname=firstname,lastname=lastname,
	contact_no=contact_no,address=address,dob=dob,gender=gender)

	return render(request,"citizen/login.html")


def login(request):
	if "c_email" in request.session:
		uid=User.objects.get(email=request.session['c_email'])
		cid=citizen.objects.get(user_id=uid)
		data=law.objects.all()
		context={
				'data':data,
				'uid':uid,
				'cid':cid,				
		}
		return render(request,"citizen/index.html",{'context':context})
	else:
		return render(request,"citizen/login.html")

def login_evaluate(request):
	if "c_email" in request.session:
		uid=User.objects.get(email=request.session['c_email'])
		cid=citizen.objects.get(user_id=uid)
		data=law.objects.all()
		context={
				'uid':uid,
				'cid':cid,
				'data':data,
		}
		return render(request,"citizen/index.html",{'context':context})
	else:	
		try:
			role=request.POST['role']
			try:
				u_email=request.POST['email']
				u_password=request.POST['password']
				uid=User.objects.get(email=u_email)
				
				if uid.role=="citizen":
					cid=citizen.objects.get(user_id=uid)
					if uid.password==u_password:
						request.session['c_email']=u_email
						data=law.objects.all()
						context={
							'data':data,
							'uid':uid,
							'cid':cid,
						}
						return render(request,"citizen/index.html",{'context':context})
					else:
						e_msg="Incorrect Password"
						return render(request,"citizen/login.html",{'e_msg':e_msg})
				elif uid.role=="commissioner":
					pass
				elif uid.role=="inspector":
					pass
				else:
					e_msg="select role"
					return render(request,"citizen/login.html",{'e_msg':e_msg})
			except:
				e_msg="Invalid email or password"
				return render(request,"citizen/login.html",{'e_msg':e_msg})
		except:
			e_msg="Select Role"
			return render(request,"citizen/login.html",{'e_msg':e_msg})

def logout(request):
	if "c_email" in request.session:
		del request.session['c_email']
		print("------------------> logout")
		return render(request,"citizen/login.html")
	else:
		return render(request,"citizen/login.html")

def law_details(request):
	return render(request,"citizen/index.html")

def citizen_dashboard(request):
	if "c_email" in request.session:
		uid=User.objects.get(email=request.session['c_email'])
		cid=citizen.objects.get(user_id=uid)
		context={
				'cid':cid,
				'uid':uid,
		}				
		return render(request,"citizen/citizen_dashboard.html",{'context':context})

def citizen_profile(request):
	pass
	# if "c_email" in request.session:
	# 	uid=User.objects.get(email=request.session['c_email'])
	# 	cid=citizen.objects.get(user_id=uid)
	# 	context={
	# 			'cid':cid,
	# 			'uid':uid,
	# 	}
	# 	return render(request,"citizen/citizen_dashboard.html",{'context':context})
	# else:
	# 	return render(request,"citizen//login.html") 

def add_fir(request):
	if "c_email" in request.session:
		uid=User.objects.get(email=request.session['c_email'])
		cid=citizen.objects.get(user_id=uid)
	context={
			'cid':cid,
			'uid':uid,
	}				
	return render(request,"citizen/add_fir.html",{'context':context})

def add_complaint(request):
	if "c_email" in request.session:
		uid=User.objects.get(email=request.session['c_email'])
		cid=citizen.objects.get(user_id=uid)
	context={
			'cid':cid,
			'uid':uid,
	}				
	return render(request,"citizen/add_complaint.html",{'context':context})

def submit_complaint(request):
	if "c_email" in request.session:
		uid=User.objects.get(email=request.session['c_email'])
		cid=citizen.objects.get(user_id=uid)
						
		complaint_title= request.POST['complaint_title']
		complaint_description= request.POST['complaint_description']
		complaint_no=cid.contact_no[-3:]+str(cid.id)

		print("------------------->",complaint_no)

		if "proof_img" in request.FILES and "proof_video" in request.FILES:
			proof_img=request.FILES['proof_img']
			proof_video=request.FILES['proof_video']
			complaint_id=complaint.objects.create(citizen_id=cid,complaint_title=complaint_title,complaint_description=complaint_description,
			complaint_no=complaint_no,proof_img=proof_img,proof_vid=proof_video)

		elif "proof_video" in request.FILES:
			proof_video=request.FILES['proof_video']
			complaint_id=complaint.objects.create(citizen_id=cid,complaint_title=complaint_title,complaint_description=complaint_description,
			complaint_no=complaint_no,proof_vid=proof_video)

		elif "proof_img" in request.FILES:
			proof_img=request.FILES['proof_img']
			complaint_id=complaint.objects.create(citizen_id=cid,complaint_title=complaint_title,complaint_description=complaint_description,
			complaint_no=complaint_no,proof_img=proof_img)
			
		else:
			complaint_id=complaint.objects.create(citizen_id=cid,complaint_title=complaint_title,complaint_description=complaint_description,
			complaint_no=complaint_no)
			

		context={
				'cid':cid,
				'uid':uid,
		}
		

		return render(request,"citizen/citizen_dashboard.html",{'context':context})

def forgot_password(request):
	if request.method=="POST":
		email=request.POST['email']	
		try:
			user=User.objects.get(email=email)
			cid=citizen.objects.get(user_id=user)
			otp=randint(1111,9999)
			user.otp=otp
			user.save()
			sendmail("Forgot Password",'mail_template',email,{'name':cid.firstname,'otp':otp})
			return render(request,'citizen/verify_otp.html',{'email':email})
		except Exception as e:
			print("------------->",e)
			e_msg="Email does not exist"
			return render(request,'citizen/forgot_password.html',{'e_msg':e_msg})

	return render(request,"citizen/forgot_password.html")

def verify_otp(request):
	otp=request.POST['otp']
	email=request.POST['email']
	uid=User.objects.get(email=email)
	if str(uid.otp)==otp:
		return render(request,"citizen/enter_new_password.html",{'email':email})
	else:
		e_msg="invalid otp"
		return render(request,"citizen/verify_otp.html",{'e_msg':e_msg,'email':email})
	

def enter_new_password(request):
	try:
		email=request.POST['email']
		newpassword=request.POST['newpassword']
		cnewpassword=request.POST['cnewpassword']
		if newpassword==cnewpassword:
			user=User.objects.get(email=email)
			user.password=newpassword
			user.save()
			return render(request,'citizen/login.html')
		else:
			e_msg="New Password & Confirm New Password Does Not Matched"
			return render(request,'citizen/enter_new_password.html',{'e_msg':e_msg})
	except:

		return render(request,"citizen/forgot_password.html")
