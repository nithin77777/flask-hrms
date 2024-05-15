from db import db
# from schemas import signupSchema
from models import userModel
from forms import signupForm

from flask.views import MethodView # For craeting views
from flask import render_template,redirect,url_for,jsonify,request,flash
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_smorest import abort
from flask_smorest.blueprint import Blueprint
# from flask_login import login_required, logout_user 
# from blps.login import blp as Loginblp


blp = Blueprint('blpSignup',__name__,description="Blueprint for signup")

@blp.route('/signup')
class signupview(MethodView):
    
    def get(self):
        form = signupForm(request.form)
        return render_template('signup.html',form=form)
    
   
    def post(self):

        form = signupForm(request.form)
        pwd_hashed = generate_password_hash(form.password.data).decode('utf-8')
        if form.validate():
            print("Form is Validated")
            # print(form.data)
            user_data = userModel(
                username = form.username.data,
                # password = form.password.data,
                password_hashed = pwd_hashed,
                pan_card = form.pan_card.data,
                identity_card = form.identity_card.data,
                job_role = form.job_role.data,
                salary = form.salary.data,
                joining_date = form.joining_date.data

                )
            
            db.session.add(user_data)
            db.session.commit()
            flash('Registration successful!')
            return redirect(url_for('blplogin.loginview'))
        else:
            flash(f'ERROR: {form.errors}')
        return render_template('signup.html',form=form)

            


