from typing import Annotated

from fastapi import Depends

import models
from services.base_service import BaseService


class LocationService(BaseService):
    def __init__(self, db: models.Db):
        super(LocationService, self).__init__(db)

    def get_all_locations(self):
        return self.db.query(models.Location).all()


def init_location_service(db: models.Db):
    return LocationService(db)


LocationServ = Annotated[LocationService, Depends(init_location_service)]
