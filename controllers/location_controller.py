from fastapi import APIRouter

import models
from dtos.location import AddNewLocationReq, AddNewLocationRes
from services.location_service import LocationServ

router = APIRouter(
    prefix='/api/v1/locations',
    tags=['locations']
)

"""

name: "sdlkjfsdlkdsfjsdfl",
"address": "ldskjfdlsdfkjfsdlkfsd",
"zip_code": "sdlkfdjsdlfkfjdsl"

"""


@router.get('/')
async def get_all_locations(location_service: LocationServ):
    locations = location_service.get_all_locations()
    return {'locations': locations}


@router.post('/', response_model=AddNewLocationRes)
# should be in a service
async def add_new_location(req: AddNewLocationReq, ):
    location = models.Location(**req.model_dump())
    # location = models.Location(name=req.name, address=req.address, zip_code=req.zip_code)

    db.add(location)
    db.commit()

    return location
