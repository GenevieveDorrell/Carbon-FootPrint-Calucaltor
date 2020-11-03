import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from pymongo import MongoClient
#import config
import logging
from forms import LoginForm
from flask_wtf.csrf import CSRFProtect
#from flask_restful import reqparse
from testToken import generate_auth_token, verify_auth_token
from password import hash_password, verify_password
from flask_login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin,
                            confirm_login, fresh_login_required)




UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'gpx'}

#flask app home base
csrf = CSRFProtect()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
csrf.init_app(app)


#CONFIG = config.configuration()

#app.secret_key = CONFIG.SECRET_KEY
#api = Api(app) #make api
client = MongoClient('mongodb://localhost:27017/data')
db = client.tododb
Userdb = client.todouserdb

# step 1 in slides
login_manager = LoginManager()
login_manager.setup_app(app)

# step 6 in the slides
login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"

# step 2 in slides
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

#end of paste setup

@app.route('/reset', methods=['GET', 'POST'])
@login_required
@csrf.exempt
def reset():
    db.tododb.drop()
    return redirect('/')
#begining of paste

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = LoginForm()
    user = form.username.data
    app.logger.debug("user: {}".format(user))
    if form.validate_on_submit():
        if Userdb.todouserdb.find({"username": user},{}).count() == 0:
            pas = hash_password(form.password.data)
            id = Userdb.todouserdb.count({})
            item_doc = {
                        'id' : id,
                        'username': user,
                        'password': pas,
                        'token': ''
                    }
            Userdb.todouserdb.insert_one(item_doc)
            one = Userdb.todouserdb.find_one({"username": user})
            app.logger.debug("userob: {}".format(one['id']))
            return redirect(url_for("login"))
        else:
            flash("that username is already taken")
    one = Userdb.todouserdb.find_one({"username": user})
    app.logger.debug("userob: {}".format(one))
    return render_template('register.html',  title='Register', form=form)
# step 3 in slides

# This is one way. Using WTForms is another way.
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        username = form.username.data
        if Userdb.todouserdb.find({"username": username}).count() == 1:
            dbuser = Userdb.todouserdb.find_one({"username": username})
            if verify_password(form.password.data, dbuser['password']):
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
    flash('lets put some stuff here')
    if request.method == 'POST': # is activated when a file is uploaded
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                global filename
                filename = secure_filename(file.filename) # security protocol
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # save uploaded file
                #return redirect(url_for('get_dir'))
            else:
                flash('Please Upload a .gpx type file')
    return render_template('home.html')

@app.route('/directions', methods=['POST', 'GET'])#home page
def get_dir():
    flash('we are working on your route please give us a second :)')
    try:
        latlon = get_latlon((UPLOAD_FOLDER + "/" + filename)) # parse file
        flash('okay here are your directions happy travels')
        directionsList = get_directions(latlon) # calcualte directions
        for direction in directionsList:
            flash(direction) #display directions
        os.remove((UPLOAD_FOLDER + "/" + filename)) # remove uploaded file
    except:
        flash("Opps something went wrong no uploaded file was found")
    return render_template('directions.html')

def allowed_file(filename): #checks if it is the correct file type
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
