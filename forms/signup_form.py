from wtforms import Form, StringField, SubmitField, IntegerField, validators, BooleanField,DateField,PasswordField


class signupForm(Form):
    username= StringField("username",[validators.Length(min=5,max=12)])
    password=PasswordField("Enter Password",[validators.Length(max=20,min=1)])
    confirm_password= PasswordField("Confirm Password",[validators.EqualTo('password')])
    identity_card= StringField("AGT ID",[validators.Length(min=1,max=7)])
    pan_card=StringField("Pan Card",[validators.Length(max=7)])
    job_role=StringField("Job Role",[validators.Length(min=1,max=7)])
    salary=IntegerField("Your Salary",[validators.NumberRange(min=10000)])
    joining_date=DateField(label="Date Joined",format="%Y-%m-%d")
    submit = SubmitField('Signup')





