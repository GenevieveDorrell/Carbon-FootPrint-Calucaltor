python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
python3 -m venv env
python3 getApiKey.py
source env/bin/activate
pip install -r requirements.txt
source run.cmd