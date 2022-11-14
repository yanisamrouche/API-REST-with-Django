from ninja import NinjaAPI, Schema
from .models import User
from typing import List
from django.shortcuts import get_object_or_404
from ninja_extra import NinjaExtraAPI, api_controller, http_get

#api = NinjaAPI()
api = NinjaExtraAPI()

class UserIn(Schema): #input payload --> CREATE
    first_name: str
    last_name: str
    gender: str
    email: str
class UserOut(Schema):#output response--> READ
    id: int
    first_name: str
    last_name: str
    gender: str
    email: str
@api_controller('/', tags=['User'], permissions=[])
class UserAPI:
    @api.get('/users', response=List[UserOut])
    def get_users(request):
        users_list = User.objects.all()
        return users_list
    @api.get('/users/{user_id}',response=UserOut)
    def get_user(request, user_id: int):
        user = get_object_or_404(User, id=user_id)
        return user
    @api.post("/users")
    def create_user(request, payload: UserIn):
        user = User.objects.create(**payload.dict())
        created_user = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "gender": user.gender,
            "email": user.email
        }
        return created_user
    @api.put("/users/{user_id}")
    def update_user(request, user_id: int, payload: UserIn):
        user = get_object_or_404(User, id=user_id)
        for attr, value in payload.dict().items():
            setattr(user, attr, value)
        user.save()
        return {"success": True}

    @api.delete("/users/{user_id}")
    def delete_user(request, user_id: int):
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return {"success": True}


api.register_controllers(
    UserAPI
)