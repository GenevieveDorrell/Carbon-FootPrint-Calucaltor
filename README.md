# Student Carbon Foot Print Calcualtor 

## Info-
According to the [New York Times](https://www.nytimes.com/guides/year-of-living-better/how-to-reduce-your-carbon-footprint), some of the largest sources of individual carbon emission are from transportation, diet, home electricity use, and consumer habits. This student carbon footprint calculator is here to help collge students understand, track, and reduce their carbon emissions over time!

## Setup-
### Heroku hosted website (recommended):
We have this application have running on heroku [here](https://student-carbon-footprint-calc.herokuapp.com/). It uses mongoDB cluters to keep track of users information. 
### Building and deploying yourself:
If you deploy this else where you must connect to a mongo database. During the build the comandline will ask for a mongodb server url. If you have mongogBD insalled on the computer or server you are deplyign the code on you can just enter 'mongodb://db:27017/'. You can also connect to a cluster like we did for our deplyment. This makes instaliation of mongoDB optional. To connect to a batabase on a cluster you must first create an account [here](https://www.mongodb.com/), and then follow the directions to to get the url connect to you cluster. It might ask you to out the databases name in the url you can put anyting you like.

**Windows**
1. Run the windowBuild.bat ('.\windowBuild.bat') to build a virtual environment and start running the program
2. To restart the application but not rebuild the entire environment run '.\windows_rerun.cmd'
3. Te exit the virual environment type 'deactivate'. Alternative there is a stop.cmd script

**MacOS**
1. Run UnixBuild.sh ('sh UnixBuild.sh') to build a virtual environment and start running the program
2. To restart the application but not rebuild the entire environment run 'source unix_rerun.cmd'
3. Te exit the virual environment type 'deactivate'. Alternative there is a stop.cmd script

## Usage- 
The website allows you to enter in various attributes in your life to calculate how much carbon you use on a day and a (projected) year. If you register an account, you can calculate your carbon over multiple days to get tracking statistics and comparisons against the average college student.

## Requirements-
You must have python and pip preinstalled on your computer for the build scripts to work. Our web aplication will then build the virtual environment and install these third party packages within the environment. 
- geopy
- Flask
- gpxpy
- wheel
- pymongo
- dnspython
- Flask-PyMongo
- Flask-WTF
- WTForms
- passlib
- Flask-Login
- gunicorn
- datetime
- plotly
- requests
- psutil
- kaleido

## Files & Directories-

* Food.py .
-Calcualtes carbon footprint based on users diet type

* Consumer.py 
-Calcualtes carbon footprint based on users shopping habits 

* Travel.py .
-Calcualtes carbon footprint based on users travel

* avg_carbon.py 
-Creates agraph of the users carbon footprint overtime

* Forms.py 
-using flaskforms it creates froms for the htmls pages

* Token.py .
-gives the user a token and loggs them out after a certian ammount of time

* Password.py 
-Hashes a users password for storage in the database as well as verifying the user is logging in with the correct password

* getMongoDB.py
-puts the database server url in mongoDB_url.txt and fetches the database url from mongoDB_url.txt

* webApp.py
-Contains code for the main web interface of the project.

* static/
-Contains the css style sheet for the web GUI, as well as users figures and website graphics.

* templates/
-Contians the home html page.

## Testing-
Each individualt python file in the backend can be run as main to get automated unit testing. (ex. python Food.py)
## Acknowledgments-
The electricity and carbon estimations based on certain activities were based on the following sources:

April 5, 2. (2019, November 19). Does Bus Transit Reduce Greenhouse Gas Emissions? Retrieved November 04, 2020, from https://reason.org/commentary/does-bus-transit-reduce-greenhouse/

Fashion Footprint Calculator. (n.d.). Retrieved November 12, 2020, from https://www.thredup.com/fashionfootprint

Frequently Asked Questions (FAQs) - U.S. Energy Information Administration (EIA). (n.d.). Retrieved November 04, 2020, from https://www.eia.gov/tools/faqs/faq.php?id=74

How Clean is Your Electric Vehicle? (n.d.). Retrieved November 07, 2020, from https://evtool.ucsusa.org/

How Much Electricity on Average Do Homes in Your State Use? (Ranked by State). (n.d.). Retrieved November 04, 2020, from https://www.electricchoice.com/blog/electricity-on-average-do-homes/

Pearce, F. (2019, May 23). In store or online - what's the environmentally friendliest way to shop? Retrieved November 08, 2020, from https://ensia.com/features/environmental-cost-online-shopping-delivery/

The carbon foodprint of 5 diets compared. (n.d.). Retrieved November 04, 2020, from http://shrinkthatfootprint.com/food-carbon-footprint-diet


