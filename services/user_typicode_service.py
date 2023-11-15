import requests

import models
from services.base_service import BaseService


class UserService(BaseService):
    def __init__(self, db: models.Db):
        super(UserService, self).__init__(db)

    def get_all_users(self):
        request = requests.get('https://jsonplaceholder.typicode.com/users')
        users = request.json()
        return users
