from src.models.disability_type import DisabilityType
from src.models.resume_offer import ResumeOffer
from src.models.resume import Resume
from src.models.experience import Experience
from src.models.offer import Offer
from src.models.organization import Organization
from src.models.profession import Profession
from src.models.user import User
from flask_admin.contrib.sqla import ModelView
from src.models.worker_notification import WorkerNotification
from settings.database.database_connection import DATABASE_URL_FOR_ADMIN
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_basicauth import BasicAuth
from flask_admin import Admin
from flask import redirect, url_for
auth = BasicAuth()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL_FOR_ADMIN
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'
app.config['BASIC_AUTH_USERNAME'] = 'admin123'
app.config['BASIC_AUTH_PASSWORD'] = 'admin123'
app.config['BASIC_AUTH_FORCE'] = False
app.config['SECRET_KEY'] = "mysecret"

bd = SQLAlchemy(app)
admin = Admin(name='ADMINKA', template_mode='bootstrap3')

auth.init_app(app)
admin.init_app(app)

with app.app_context():
    admin.add_view(ModelView(DisabilityType, session=bd.session))
    admin.add_view(ModelView(Experience, session=bd.session))
    admin.add_view(ModelView(Offer, session=bd.session))
    admin.add_view(ModelView(Organization, session=bd.session))
    admin.add_view(ModelView(Profession, session=bd.session))
    admin.add_view(ModelView(ResumeOffer, session=bd.session))
    admin.add_view(ModelView(Resume, session=bd.session))
    admin.add_view(ModelView(User, session=bd.session))
    admin.add_view(ModelView(WorkerNotification, session=bd.session))


if __name__ == "__main__":
    app.run(debug=True)