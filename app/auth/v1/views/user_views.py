from flask import request, jsonify
from flask_restful import Resource, reqparse
from app.auth.v1.models.user_models import UserModel, Code_problemsModel, Search_code_problem,language

user_model_view = UserModel()
user_model_view = Code_problemsModel()
user_model_view=Search_code_problem()
user_model_view=language()

class UserRegister(Resource):
    """
    User class view for register endpoint
    """

    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True, help="Please input an email")
    parser.add_argument("username", type=str, required=True, help="Please input your name")

    def post(self):
        """
        HTTP method to register a new user
        """
        try:
            args = UserRegister.parser.parse_args()
            args = request.get_json()
            new_user = user_model_view.create_user(
                username=args['username'],
                email=args['email'],
                password=args['pasTypeError: exceptions must derive from BaseExceptionsword'],
                confirm_password=args['confirm_password']
                )


        except Exception as e:
            return {
                "status": 400,
                "error": "Invalid Key error {}".format(e)
            }, 400

        return {
            "status": 201,
            "data": new_user
        }, 201

class Code_problems(Resource):
    '''
    This is a class for code problems end point
    '''
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=True, help="Please input the title")
    parser.add_argument("language", type=str, required=True, help="Please input the language of your coding problem")
    parser.add_argument("content",type=str, required=True, help= "Please Enter your coding problem")

    def post(self):
        '''
        HTTP request to create a Coding Problem
        '''
        args=Code_problems.parser.parse_args()
        args = request.get_json()
        # import pdb; pdb.set_trace()
        new_codep = user_model_view.create_codep(
                self,
                title=args['title'],
                language=args['language'],
                content=args['content']
            )

        return {
            "status": 201,
            "data": new_codep
        }, 201

    # def delete(self):
    #     '''this deletes'''
    #     del Code_problems[codeId]

    # unfinished--------------------------
class Search_code_problem(Resource):
        def get(self):
            return jsonify({'Code_problems':Search_code_problem})

class language(Resource):
    def post(self):
        args=language.parser.parse_args()
        args=request.get_json()
        new_lang=user_model_view.create_lang(
            self,
            language=args['language']
        )

        return {
                "status": 201,
                "data": new_lang
            }, 201

    def get(self):
        return jsonify(self)