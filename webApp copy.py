import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from gpx_parser import get_latlon
from directions import get_directions

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'gpx'}

#flask app home base

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['POST', 'GET'])#home page
def home():
    flash('Upload a .gpx file')
    flash('It may take us a second to calucalte your route so please be patient')
    if request.method == 'POST': # is activated when a file is uploaded
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                global filename
                filename = secure_filename(file.filename) # security protocol
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # save uploaded file
                return redirect(url_for('get_dir'))               
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
