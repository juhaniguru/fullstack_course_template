

from fastapi import APIRouter

import models
from services.inspection_target_service import TargetServ

router = APIRouter(
    prefix='/api/v1/targets',
    tags=['target']
)

@router.get('/')
async def get_all_targets(service: TargetServ):
    targets = service.get_all()
    return {'targets': targets}