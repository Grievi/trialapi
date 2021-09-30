from app.auth.v1.models.user_models import language
from flask import Blueprint
from flask_restful import Api
from .views.user_views import Code_problems, UserRegister, Search_code_problem,language

version_1_auth = Blueprint('auth_v1', __name__, url_prefix='/auth/v1')

api = Api(version_1_auth)

api.add_resource(UserRegister, '/signup')
api.add_resource(Code_problems, '/codeproblems')
api.add_resource(Search_code_problem, '/searchcodeproblem')
api.add_resource(language, '/language')