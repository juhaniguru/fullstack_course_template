import models
from services.base_service import BaseService


class UserService(BaseService):
    def __init__(self, db: models.Db):
        super(UserService, self).__init__(db)

    def get_all_users(self):
        users = self.db.query(models.User).all()
        return users