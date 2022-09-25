from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
ALPHANUMERIC = re.compile(r"^[a-zA-Z0-9]+$")

class Dojo:
    def __init__(self , data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # CREATE METHOD
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s)"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # VALIDATOR
    @staticmethod
    def validate(data):
        print(data)
        is_valid = True
        if len(data['name']) < 1:
            is_valid = False
            flash('Name must be provided', 'err_dojo_name')
        elif not ALPHANUMERIC.match(data['name']):
            flash('Name cannot contain special chars', 'err_dojo_name')
            is_valid = False
        if data['location'] == 'default':
            flash("Please pick a non default location", 'err_dojo_location')
            is_valid = False
        if data['language'] == 'default':
            flash("Please pick a non default language", 'err_dojo_language')
            is_valid = False
        if len(data['comment']) < 1:
            is_valid = False
            flash("Comment must be provided", 'err_dojo_comment')
        return is_valid

