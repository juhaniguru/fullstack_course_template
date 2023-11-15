from fastapi import APIRouter

import models
from services.environment_service import EnvironmentServ

router = APIRouter(
    prefix='/api/environments',
    tags=['environment']
)


@router.get('/')
async def get_all_environments(service: EnvironmentServ):
    environments = service.get_all()
    return {'environments':environments}
