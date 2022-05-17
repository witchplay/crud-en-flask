from app import app
from utils.db import db
from models.models import login

with app.app_context():
    db.create_all()

login.init_app(app)
login.login_view = 'login'
login.login_message = 'Por favor inica sesión para acceder a esta página.'



if __name__ == '__main__':
    app.run(port=5000, debug=True)