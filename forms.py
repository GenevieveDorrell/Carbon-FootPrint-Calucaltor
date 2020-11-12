  
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('sign in')
    register = SubmitField('create account')


class CarbonFootprint(FlaskForm):
    food = SelectField('Diet', choices=[('vegan', 'vegan'), ('vegetarian', 'vegetarian'),
     ('white_meat_only', 'white meat only'), ('med_meat', 'medium meat'), ('high_meat', 'high meat')])
    travel_method = SelectField('Transproation', choices=[('gcar','gas car'),('hcar', 'hybrid car'),('bus', 'bus'),('non_motor', 'walk or bike')])
    distance = IntegerField('Daily Commute', validators=[DataRequired()])
    housing = SelectField('Housing', choices=[('dorm', 'dorm'),('off_apartment','apartment'),('off_house','house')])
    numRooms = IntegerField('Rooms', validators=[DataRequired()])
    numRoomates = IntegerField('Roomates', validators=[DataRequired()])
    numPackages = IntegerField('Number of Packages', validators=[DataRequired()])
    track_submit = SubmitField('Track Carbon Footprint')
    submit = SubmitField('Calculate Carbon Footprint')
    delete = SubmitField('Delete Acount')
    fast_delivery = BooleanField("Fast delivery")
    packages = IntegerField('number of packages ordered per month', validators=[DataRequired()])
    used_clothing = IntegerField('Percent of Wardrobe bought used', validators=[DataRequired()])#add min and max
    clothing_purchased = IntegerField('number of clothing items perchased per month', validators=[DataRequired()])