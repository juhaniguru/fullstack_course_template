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
async def add_new_location(req: AddNewLocationReq, location_service: LocationServ):
    
    location = location_service.add(req)

    return location

@router.get('/{id}', response_model=AddNewLocationRes)
async def get_location_by_id(id:int, location_service: LocationServ):
    return location_service.get_by_id(id)