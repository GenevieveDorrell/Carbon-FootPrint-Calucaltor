# Carbon Foot Print Calcualtor 

## Info-
TODO

## Setup-
First have mongo DB installed on your computer or server. If you need to install it a free community version is avialable here https://www.mongodb.com/try/download/community.
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
The electricity and carbon estimations based on certain activities were based on the following sources:

April 5, 2. (2019, November 19). Does Bus Transit Reduce Greenhouse Gas Emissions? Retrieved November 04, 2020, from https://reason.org/commentary/does-bus-transit-reduce-greenhouse/

The carbon foodprint of 5 diets compared. (n.d.). Retrieved November 04, 2020, from http://shrinkthatfootprint.com/food-carbon-footprint-diet

Frequently Asked Questions (FAQs) - U.S. Energy Information Administration (EIA). (n.d.). Retrieved November 04, 2020, from https://www.eia.gov/tools/faqs/faq.php?id=74

How Much Electricity on Average Do Homes in Your State Use? (Ranked by State). (n.d.). Retrieved November 04, 2020, from https://www.electricchoice.com/blog/electricity-on-average-do-homes/
