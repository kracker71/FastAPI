from fastapi import APIRouter,Depends, status
from .. import schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    tags=['blogs'],
    prefix='/blog',
    dependencies= [Depends(oauth2.get_current_user)]
    )
get_db = database.get_db


@router.get('/', response_model= List[schemas.ShowBlog],dependencies=[Depends(oauth2.get_current_user)] )
def all(db : Session = Depends(get_db)):
    return blog.get_all(db)

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    return blog.create(request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db : Session = Depends(get_db)):
    return blog.destroy(id,db)



@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db : Session = Depends(get_db)):
    return blog.update(id,request,db)
    



@router.get('/{id}',status_code=200, response_model = schemas.ShowBlog)
def show(id,db : Session = Depends(get_db)):
    return blog.show(id,db)
