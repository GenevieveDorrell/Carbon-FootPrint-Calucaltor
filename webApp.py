import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from pymongo import MongoClient
import logging
from forms import LoginForm, CarbonFootprint
from flask_wtf.csrf import CSRFProtect
from testToken import generate_auth_token, verify_auth_token
from password import hash_password, verify_password
from flask_login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin,
                            confirm_login, fresh_login_required, current_user)
from Food import food_footprt
from Home import home_footprt
from Travel import travel_footprt
from datetime import date




UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'gpx'}

#flask app home base
csrf = CSRFProtect()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
csrf.init_app(app)


client = MongoClient('mongodb://localhost:27017/data')
Userdb = client.todouserdb


login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"

@login_manager.user_loader
def load_user(user_id):
    dbuserOBj = Userdb.todouserdb.find_one({"id": user_id})
    if dbuserOBj != None:
        user = User(dbuserOBj['username'], dbuserOBj['id'])
        if user.has_valid_token():
            return user
    return None

class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def has_valid_token(self):
        dbuser = Userdb.todouserdb.find_one({"id": self.id})
        if verify_auth_token(dbuser['token']) == 'Success':
            return True
        else:
            return False

    def is_anonymous(self):
        return False

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = LoginForm()
    user = form.username.data
    if form.validate_on_submit(): #check if form is filled out and submited
        if Userdb.todouserdb.find({"username": user},{}).count() == 0: #check to see if the username is in use
            pas = hash_password(form.password.data)#hash password
            id = Userdb.todouserdb.count({})#create user
            item_doc = {
                        'id' : id,
                        'username': user,
                        'password': pas,
                        'token': ''
                    }
            Userdb.todouserdb.insert_one(item_doc)#add user to userdb
            return redirect(url_for("login"))
        else:
            flash("that username is already taken")
    return render_template('register.html',  title='Register', form=form)
# step 3 in slides

# This is one way. Using WTForms is another way.
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit(): #check if form is filled out and submited
        # Login and validate the user.
        # user should be an instance of your `User` class
        username = form.username.data # get username from form
        if Userdb.todouserdb.find({"username": username}).count() == 1: #check if the usermane in the db
            dbuser = Userdb.todouserdb.find_one({"username": username})
            if verify_password(form.password.data, dbuser['password']): #check agianst hashed pass
                user = User(username,dbuser['id'])
                login_user(user, form.remember_me.data)
                token = generate_auth_token()
                Userdb.todouserdb.update_one(dbuser, {'$set': {'token': token}})
                flash('Logged in successfully.')
                return redirect('/')
            else:
                flash('incorrect Password.')
        else:
            flash('unregistered user')
    return render_template('login.html',  title='Sign In', form=form)


# step 5 in slides
@app.route("/reauth", methods=["GET", "POST"])
@login_required
def reauth():
    if request.method == "POST":
        confirm_login()
        flash("Reauthenticated.")
        return redirect(request.args.get("next") or url_for("login"))
    return redirect(url_for("login"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("login"))
#end of paste

@app.route('/', methods=['POST', 'GET'])#home page
@login_required
def home():
    loggedin = current_user.is_active
    form = CarbonFootprint()
    if form.validate_on_submit(): #check if form is filled out and submited
        diet = form.food.data
        housing = form.housing.data
        numRooms = form.numRooms.data
        numRoomates = form.numRoomates.data
        travel_mode = form.travel_method.data
        commute = form.distance.data
        footprint = food_footprt(diet) + home_footprt(housing, 
        numRooms, numRoomates) + travel_footprt(travel_mode, commute)
        flash('you carbon foot print is '+ str(footprint) + ' lbs. of CO2/yr.')   
    return render_template('home.html', title = 'Home', form = form, loggedin = loggedin)

@app.route('/account', methods=['POST', 'GET'])#home page
@login_required
def account():
    form = CarbonFootprint()
    if form.delet.data:
            Userdb.todouserdb.delete_one({'id': current_user.id})
            return redirect(url_for("logout"))
    if form.validate_on_submit(): #check if form is filled out and submited        
        diet = form.food.data
        housing = form.housing.data
        numRooms = form.numRooms.data
        numRoomates = form.numRoomates.data
        travel_mode = form.travel_method.data
        commute = form.distance.data
        footprint = food_footprt(diet) + home_footprt(housing, 
        numRooms, numRoomates) + travel_footprt(travel_mode, commute)
        if current_user.is_active:
            Userdb.todouserdb.update_one({'id': current_user.id}, {"$set": {'housing': housing,
                                                                            'numRooms': numRooms,
                                                                            'diet': diet,
                                                                            'numRooms': numRooms,
                                                                            'travel_mode': travel_mode,
                                                                            'commute': commute}})
                                                                   #"$set": {'numRooms': numRooms},
                                                                   #"$set": {'diet': diet},
                                                                   #"$set": {'numRooms': numRooms},
                                                                   #"$set": {'numRoomates': numRoomates},
                                                                   #"$set": {'travel_mode': travel_mode},
                                                                   #"$set": {'commute': commute}})
                                                                   #"$addToSet": {'footprint': [footprint, str(date.today())]}
                                                                   #"$set":{'numRooms': numRooms}
                                                                   #"$addToSet":{'dates': date.today.strftime("%d/%m/%Y")}
                                                                   #"$addToSet":{'footprint': (footprint, date.today.strftime("%d/%m/%Y"))}})
            #dbObj = load_user(current_user.id)
            data = Userdb.todouserdb.find_one({'id': current_user.id})
            try:
                FootprintList = data['footprint']
                if FootprintList[len(FootprintList)-1][1] == str(date.today()):
                    FootprintList[len(FootprintList)-1][0] = footprint
                    Userdb.todouserdb.update_one({'id': current_user.id}, {"$set": {'footprint': FootprintList}})
                else:
                    Userdb.todouserdb.update_one({'id': current_user.id}, {"$addToSet": {'footprint': [footprint, str(date.today())]}})
            except:
                Userdb.todouserdb.update_one({'id': current_user.id}, {"$addToSet": {'footprint': [footprint, str(date.today())]}})
            print(data)
            print(data['commute'])
            print(current_user.id)
            print(current_user.name)
            print()
        flash('you carbon foot print is '+ str(footprint) + ' lbs. of CO2/yr.')   
    return render_template('account.html', title = 'Home', form = form)