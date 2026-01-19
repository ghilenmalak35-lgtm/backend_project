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
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Create_user(BaseModel):
    name: str
    email: str
    password:str
    role: str
  

   
