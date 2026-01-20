###
#from pydantic import BaseModel
#class Create_user(BaseModel):
  #  id:int
   # name:str
   # email:str
   # password:str
    #role:str
    #is_active:str
    #last_login:str
   # created_at:str
   # updated_at:str
    #deleted_at:str
###
from pydantic import BaseModel,constr
class Create_user(BaseModel):
    name: str
    email: str
    password:constr(min_length=8, max_length=72)
    role: str
  
class User_login(BaseModel):
    password:str
    email:str
   
