python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
python3 -m venv env
python3 getMongoDB.py
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=webApp.py
python -m flask run