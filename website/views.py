from flask import Blueprint,render_template,request,redirect
from asyncio.windows_events import NULL
from flask import flash
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import update
import datetime
from website.models import Blood ,Lastdonationdate
from website import db
from flask_login import  login_required , current_user

views = Blueprint('views',__name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/search_blood',methods=['GET','POST'])
def search_blood():
    if request.method == 'POST':
        searchbyblood = request.form.get("searchbyblood")
        donors = Blood.query.filter_by(bloodgroup=searchbyblood).all()
        return render_template('search_blood.html', donors = donors)

    return render_template("search_blood.html")

@views.route('/editdashboard',methods=['GET','POST'])
@login_required
def editdashboard():
    if request.method == 'POST':
        uname = request.form.get("uname")
        sex =request.form.get("sex")
        bloodgroup = request.form.get("bloodgroup")
        address = request.form.get("address")
        city = request.form.get("city")
        email = request.form.get("email")
        contact = request.form.get("contact")

        blood = Blood.query.filter_by(email=email).first()
        blood.uname=uname
        blood.sex=sex
        blood.bloodgroup=bloodgroup
        blood.address=address
        blood.city=city
        blood.email=email
        blood.contact=contact

        db.session.commit() 

    return render_template('editdashboard.html',user=current_user)

@views.route('/userdashboard')
@login_required
def userdashboard():
    return render_template('userdashboard.html',user=current_user)

@views.route('/admindashboard')
@login_required
def admindashboard():
    return render_template('admindashboard.html',user=current_user)

@views.route('/admineditdashboard')
@login_required
def admineditdashboard():
    donors = Blood.query.all()
    donors.pop(1)
    return render_template('admineditdashboard.html',donors=donors,user=current_user)


@views.route('/changepassword',methods=['GET','POST'])
@login_required
def changepassword():
    if request.method == 'POST':
        password = request.form.get("password")
        password1 = request.form.get("password1")
        if(password == password1):
            email = request.form.get("email")
            blood = Blood.query.filter_by(email=email).first()
            blood.password=password
            db.session.commit()
            flash('password updated successfully', category='sucess')
        else:
            flash('passwords don\'t match', category='error')

    return render_template('changepassword.html',user=current_user)

@views.route('/lastdonationdate')
@login_required
def lastdonationdate():
    return render_template('lastdonationdate.html',user=current_user)

@views.route('/uploadhealthcertificate')
@login_required
def uploadhealthcertificate():
    return render_template('uploadhealthcertificate.html',user=current_user)


@views.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        uname = request.form.get("uname")
        password = request.form.get("password")
        password1 = request.form.get("password1")
        dob1 = request.form.get("dob")
        dob2 = datetime.datetime.strptime(dob1, "%Y-%m-%d")
        sex = request.form.get("sex")
        bloodgroup = request.form.get("bloodgroup")
        address = request.form.get("address")
        city = request.form.get("city")
        email = request.form.get("email")
        contact = request.form.get("contact")
        
        if len(uname) < 2:
            flash('Name  must be greater than 1 characters', category='error')
        elif len(password1) < 7:
            flash('passwords must be atleast 7 characters', category='error')    
        elif password != password1:
            flash('passwords don\'t match', category='error')
        elif (dob1 == NULL ): 
            flash('dob must be filled', category='error')    
        elif (sex == "Select"): 
            flash('sex must be filled', category='error')
        elif (bloodgroup == "Select"): 
            flash('bloodgroup must be filled' , category ='error') 
        elif (address == NULL): 
            flash('address must be filled' , category='error')  
        elif (city == NULL): 
            flash('city must be filled' ,category='error') 
        elif len(email) < 2:
            flash('email must be greater than 5 characters',category='error')                        
        elif len(contact) != 10:
            flash('contact must conatain 10 characters',category='error')
        else:
            flash('Account created', category='sucess')
            blood = Blood(uname=uname,password=password,dob=dob2,sex=sex,bloodgroup=bloodgroup,address=address,city=city,email=email,contact=contact)
            db.session.add(blood)
            db.session.commit()  
        return render_template('register.html') 
    return render_template("register.html")      