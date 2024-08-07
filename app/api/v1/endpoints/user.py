from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.user import UserCreate, UserUpdate, UserResponse,UserLogin
from app.services.user_service import create_user, get_user, get_users, update_user, delete_user, authenticate_user

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=List[UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.put("/{user_id}", response_model=UserResponse)
def update_existing_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    deleted = delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
@router.post('/login',response_model=UserResponse)
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db,user_credentials.email, user_credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# @router.get("/{id}")
# async def get_user_by_id(id):
#     return {"message":f'user with  id {id}'}

# if we use this after /{id},then this will not accessed ,user/{id} will be accessed...so order is important
# @router.get("/all")
# async def get_user_all():
#     return {"message":'all user list'}

# #query parameters
# @router.get('/all')
# def get_all_users(page,pageSize):
#     return {'message':f'All {pageSize} users on page {page}'}

# #default value parameter
# @router.get('/all')
# def get_all_users(page=1,pageSize=10):
#     return {'message':f'All {pageSize} users on page {page}'}

# #optional parameter
# @router.get('/all')
# def get_all_users(page=1,pageSize:Optional[int]=None):
#     return {'message':f'All {pageSize} users on page {page}'}

# #path parameter and query parameter together
# @router.get('/{id}/comments/{comment_id}')
# def get_comments(id:int,comment_id:int, valid:bool = True ,username:Optional[str]=None):
#     return {'message':f'user id {id}, comment id {comment_id},valid {valid}, username {username}'}

# class UserType(str,Enum):
#     section='section'
#     subject='subject'
#     session='session'
# @router.get("/type/{type}")
# def get_user_type(type:UserType):
#     return {'message':f'user type {type}'}

# @router.get("/{id}",status_code=status.HTTP_200_OK)
# #type validation
# async def get_user_by_id(id:int,response:Response):
#     if id>5:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {'error':f'received user id {id} not found'}
#     else:
#         response.status_code = status.HTTP_200_OK
#         return {"message":f'user with  id {id}'}