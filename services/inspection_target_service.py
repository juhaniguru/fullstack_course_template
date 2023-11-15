from typing import Annotated

from fastapi import Depends

import models
from services.base_service import BaseService


class TargetService(BaseService):
    def __init__(self, db: models.Db):
        super(TargetService, self).__init__(db)

    def get_all(self):
        return self.db.query(models.Inspectiontarget).all()


def init_target_service(db: models.Db):
    return TargetService(db)


TargetServ = Annotated[BaseService, Depends(init_target_service)]


