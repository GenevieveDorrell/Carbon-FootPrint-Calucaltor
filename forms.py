  
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    register = SubmitField('Register')

class CarbonFootprint(FlaskForm):
    food = SelectField('Diet prefrence', choices=[('vegan', 'vegan'), ('vegetarian', 'vegetarian'),
     ('white_meat_only', 'white meat only'), ('med_meat', 'medium meat'), ('high_meat', 'high meat')])
    travel_method = SelectField('Mode of transproation', choices=[('car'),('bus'),('bike'),('walk')])
    distance = IntegerField('Distance traveled', validators=[DataRequired()])
    housing = SelectField('Housing', choices=[('dorm', 'dorm'),('off_apartment','apartment'),('off_house','house')])
    numRooms = IntegerField('Number of Rooms', validators=[DataRequired()])
    numRoomates = IntegerField('Number of Roomates', validators=[DataRequired()])
    submit = SubmitField('Calcualte Carbon Footprint')