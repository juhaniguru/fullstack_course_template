from typing import Annotated

from fastapi import Depends

import models
from services.base_service import BaseService


class EnvironmentService(BaseService):
    def __init__(self, db: models.Db):
        super(EnvironmentService, self).__init__(db)

    def get_all(self):
        return self.db.query(models.Environment).all()


def init_envinronment_service(db: models.Db):
    return EnvironmentService(db)


EnvironmentServ = Annotated[BaseService, Depends(init_envinronment_service)]
