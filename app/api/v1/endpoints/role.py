from fastapi import FastAPI,APIRouter,status,Response

router = APIRouter()


@router.get("/")
def get_all_roles(response:Response):
    response.status_code = status.HTTP_200_OK
    return {'message':'all role list is fetched'}
