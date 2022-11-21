from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
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
        if len(username) < 3 and len(password) > 7 and re.match("^[a-z0-9]+$", password):
            raise UserInputError("Username was too short. Password ok!")
        
        if len(password) < 8 and len(username) > 2 and re.match("^[a-z]+$", username):
            raise UserInputError("Username ok! Password too short.")

        if len(username) > 2 and len(password) > 7 and re.match("^[a-z]+$", username) and not re.match("^[0-9]+$", password) and re.match("^[a-z]+$", password): 
            raise UserInputError("Password must contain numbers!")

        if len(username) < 3 or len(password) < 8 or not re.match("^[a-z]+$", username) or not re.match("^[a-z0-9]+$", password): 
            raise UserInputError("Username > 3, password > 8 and password should contain letters+numbers")
        