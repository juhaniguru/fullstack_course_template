from typing import Annotated

from fastapi import Depends

import models
from services.base_service import BaseService
from dtos.location import AddNewLocationReq

class LocationService(BaseService):
    def __init__(self, db: models.Db):
        super(LocationService, self).__init__(db)

    def get_all_locations(self):
        return self.db.query(models.Location).all()
    
    def add(self, req: AddNewLocationReq):

        location = models.Location(**req.model_dump())

        self.db.add(location)
        self.db.commit()

        return location
    
    def get_by_id(self, id:int):
        return self.db.query(models.Location).filter(models.Location.id == id).first()


def init_location_service(db: models.Db):
    return LocationService(db)


LocationServ = Annotated[LocationService, Depends(init_location_service)]
