import models


class BaseService:
    def __init__(self, db: models.Db):
        self.db = db

    def commit(self):
        self.db.commit()

    def add(self, entity):
        self.db.add(entity)

    def get_all(self):
        pass

    def get_by_id(self, _id: int):
        pass

    def remove(self, _id):
        pass
