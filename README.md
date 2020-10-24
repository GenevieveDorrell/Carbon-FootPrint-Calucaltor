# Reverse Geocoding 

## Info-
TODO

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
TODO

## Requirements-
You must have python and pip preinstalled on your computer for the build scripts to work. Our web aplication will then build the virtual environment and install these third party packages within the environment. 
- gpxpy
- Flask


## Files & Directories-

* gpx_parser.py .
-Parses a gpx input file and returns data

* webApp.py
-Contains code for the main web interface of the project.

* static/
-Contains the css style sheet for the web GUI

* templates/
-Contians the home html page.

* tests/
-Contians .gpx files that you can use to test your setup.

## Acknowledgments-
