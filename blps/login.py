from models import userModel
from db import db
from forms import signupForm, LoginForm

from flask import render_template,redirect,url_for,jsonify,request,flash,make_response
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_smorest import abort
from flask.views import MethodView
from flask_smorest.blueprint import Blueprint

# login requirements 
from flask_login import login_required, logout_user, login_user,current_user

blp = Blueprint('blplogin',__name__,description="Login Blueprint")


@blp.route('/login',methods=['GET','POST'])
class loginview(MethodView):
    def get(self):
        form =LoginForm(request.form)
        return render_template('login.html',form=form)
    
    def post(self):
        form = LoginForm(request.form)
        username = form.username.data
        password = form.password.data
        user_now = userModel.query.filter_by(username=username).first()
        print(user_now)
        if request.method=='POST':
            if form.validate():
                if user_now and check_password_hash(user_now.password_hashed,password=password):
                    flash("Logged In Successfully")
                    login_user(user_now,remember=True)
                    flash("Logged In Successfully")
                    return redirect(url_for('blplogin.home',username=username))
                else:
                    flash("Invalid Login credentials")
        return render_template('login.html',form=form)


@blp.route('/logout')
@login_required
def logout_employee():
    logout_user()
    flash('You Have Logged Out Successfully')
    return redirect(url_for('blplogin.loginview'))
    # return """<h1>Logged Out </h1>""" 


@blp.route('/home/<string:username>')
@blp.route('/home')
@login_required
def home(username=None):
    if not username:
        username = request.args.get('username', current_user.username)
        print(username)
    response = make_response(render_template('home.html', username=username))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = 'Fri, 01 Jan 1990 00:00:00 GMT'
    return response