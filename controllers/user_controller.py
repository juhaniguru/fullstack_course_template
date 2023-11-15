from typing import Annotated

from fastapi import APIRouter, Depends
from passlib.context import CryptContext


import models

import services.user_sa_service
import services.user_typicode_service
from dtos.user import AddNewUserReq, AddNewUserRes

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

router = APIRouter(
    prefix='/api/v1/users',
    tags=['users']
)


def init_user_service(db: models.Db):
    # should be in env file
    data_provider = 'typicode'
    if data_provider == 'mysql':
        return services.user_sa_service.UserService(db)
    else:
        return services.user_typicode_service.UserService(db)


UserServ = Annotated[services.user_sa_service.UserService, Depends(init_user_service)]


@router.get('/')
async def get_all_users(service: UserServ):
    users = service.get_all_users()
    return {'users': users}






