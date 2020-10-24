# Reverse Geocoding 

## Info-
Code Developed for reverse geocoding applications. This entails converting gps points into a cue sheet of directions. 

## Setup-
**Windows**
1. Run the windowBuild.bat ('.\windowBuild.bat') to build a virtual environment and start running the program
Note: To call run.cmd alone you must be in the virtual environment. 
2. To reenter the virtual environment after it has been built use './env\Scripts\activate.bat'
3. Te exit the virual environment type 'deactivate'. Alternative there is a stop.cmd script

**MacOS**
1. Run UnixBuild.sh ('sh UnixBuild.sh') to build a virtual environment and start running the program
Note: To call run.cmd alone you must be in the virtual environment. 
2. To reenter the virtual environment after it has been built use 'source env/bin/activate'
3. Te exit the virual environment type 'deactivate'. Alternative there is a stop.cmd script

## Usage- 
This program takes gps data in the form of a .gpx file, either from a bike ride or a walk, and recreates the users route in a cue sheet form. This way you can easily track your routes or build maps of your favorite paths!

## Requirements-
You must have python and pip preinstalled on your computer for the build scripts to work. Our web aplication will then build the virtual environment and install these third party packages within the environment. 
- utm==0.6.0
- gpxpy==1.4.2
- numpy==1.16.4
- geopy==2.0.0
- Flask==1.0.3


## Files & Directories-
* directions.py
-The main logic file. Calculates all of the streets that the route goes on, as well as distance on each street and turn direction from that street. 

* openMap_API.py
-Connects with the API to retrieve street addresses from the give gps points.

* gpx_parser.py .
-Parses a gpx input file and returns the latlon data in a list

* webApp.py
-Contains code for the main web interface of the project.

* static/
-Contains the css style sheet for the web GUI

* templates/
-Contians the home html page.

* uploads/
-Contains gpx files that the user uploads for duration of reverse geocoding process. Files are delete after use for security reasons. 

* tests/
-Contians .gpx files that you can use to test your setup.

## Acknowledgments-
This project uses reverse geocoding serveces from https://geoservices.tamu.edu/ API to convert latlon data to street addresses. 
