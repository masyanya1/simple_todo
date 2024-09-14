from flask import Flask
from blueprints import login, main_tasks
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['USERNAME'] = os.getenv('USERNAME')
app.config['PASSWORD'] = os.getenv('PASSWORD')

app.register_blueprint(login.login_view)
app.register_blueprint(main_tasks.main_tasks)

if __name__ == '__main__':
    app.run(debug=True)
