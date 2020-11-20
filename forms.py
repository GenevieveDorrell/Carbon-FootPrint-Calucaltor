
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, validators
from wtforms.validators import InputRequired, EqualTo, Length, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember Me')
    register = SubmitField('create account')
    submit = SubmitField('sign in')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=6,max=24,message="Username must be at leat 6 characters")])
    password_set = PasswordField('Password', validators=[
        InputRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password', validators=[InputRequired(),
    Length(min=6,max=24,message="Password must be at leat 6 characters")
    ])
    register = SubmitField('create account')


class CarbonFootprint(FlaskForm):
    food = SelectField('Diet', choices=[('vegan', 'vegan'), ('vegetarian', 'vegetarian'),
     ('white_meat_only', 'white meat only'), ('med_meat', 'medium meat'), ('high_meat', 'high meat')])
    travel_method = SelectField('Transportation', choices=[('gcar','gas car'),('hcar', 'hybrid car'),('bus', 'bus'),('non_motor', 'walk or bike')])
    distance = IntegerField('Daily Commute (one way)', validators=[InputRequired(), NumberRange(min=0, max=None, message="Cannot enter a negative distance")])
    housing = SelectField('Housing', choices=[('dorm', 'dorm'),('off_apartment','apartment'),('off_house','house')])
    numRooms = IntegerField('Bedrooms', validators=[InputRequired(), NumberRange(min=0, max=None, message="Cannot enter a negative distance")])
    numRoomates = IntegerField('Roomates', validators=[InputRequired(), NumberRange(min=0, max=None, message="Cannot enter a negative distance")])
    numPackages = IntegerField('Number of packages/month', validators=[InputRequired(), NumberRange(min=0, max=None, message="Cannot enter a negative distance")])
    fast_delivery = BooleanField("Fast delivery")
    used_clothing = IntegerField('% Used clothes', validators=[InputRequired(), NumberRange(min=0, max=100, message="enter a percentage ie. 0-1 or 1-100")])#add min and max
    clothing_purchased = IntegerField('Clothing items bought per month', validators=[InputRequired(), NumberRange(min=0, max=None, message="Cannot enter a negative distance")])
    track_submit = SubmitField('Track Carbon Footprint')
    submit = SubmitField('Calculate Carbon Footprint')
    delete = SubmitField('Delete Account')
<<<<<<< HEAD
=======
    
>>>>>>> d4f4ca099acb86dc09f741c1e4d6eef6ff420acf
