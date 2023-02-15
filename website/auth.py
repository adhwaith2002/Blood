from asyncio.windows_events import NULL
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint,render_template,request,redirect,url_for
import datetime
from website.models import Blood
from website import db
from flask_login import login_user , login_required , logout_user ,current_user


auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

       
        user = Blood.query.filter_by(email=email).first()
        if user:
            if(user.password == password):
                
                login_user(user, remember=True)
                if(user.email == 'admin@123'):
                    return redirect ('admindashboard')
                else:
                    return redirect('userdashboard')
            else:
                flash('incorrect password',category='error')
        else:
            flash('email does not exist',category='error')            
    return render_template("login.html")



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
