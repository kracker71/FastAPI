from fastapi import APIRouter,Depends
from blog import schemas, database
from typing import List
from sqlalchemy.orm import Session
from blog.repository import user


router = APIRouter(
        tags=['users'],
        prefix= '/user'
        )
get_db = database.get_db

@router.post('/', response_model= schemas.ShowUser)
def create_user(request: schemas.User, db : Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model= schemas.ShowUser)
def get_user(id:int, db : Session = Depends(get_db)):
    return user.show(id,db)

@router.get('/',response_model= List[schemas.ShowUser])
def get_all_users(db : Session = Depends(get_db)):
    return user.show_all(db)

