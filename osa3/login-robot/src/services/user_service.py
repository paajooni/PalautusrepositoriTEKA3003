from entities.user import User
import re
import sys, pdb


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        # pysäytetään ohjelman suoritus tälle riville
        pdb.Pdb(stdout=sys.__stdout__).set_trace()
        
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if not re.match("^[a-z]+$", username):
            raise AuthenticationError("Username must contain only lowercase letters")
        
        if len(username) < 3:
            raise AuthenticationError("Username must be at least 3 characters long")

        if len(password) < 8:
            raise AuthenticationError("Password must be at least 8 characters long")

        if not re.search(r"[0-9!@#$%^&*(),.?:{}|<>]", password):
            raise AuthenticationError("Password must contain at least one non-letter character")
        

        return "Valid"
