from fastapi import APIRouter

router = APIRouter(prefix = '/task')

@router.get('/')
def top():
    return 'top task endpoint'
