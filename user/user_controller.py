from fastapi import FastAPI, Depends, HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from .model import User
from .schema import Create_user
app = FastAPI()
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/users", tags=["users"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/createuser")
def CreateUser(userss:Create_user, db: Session = Depends(get_db)):
    userss = User(name=userss.name,email=userss.email,password=userss.password,role=userss.role)
    db.add(userss)
    db.commit()
    db.refresh(userss)
    return userss
@router.get("/userList")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
@router.get("/users/{user_id}", response_model=Create_user)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Users non trouvé")
    return user
@router.get("/user/{user_name}", response_model=Create_user)
def get_username(user_name:str, db: Session = Depends(get_db)):
    usere = db.query(User).filter(User.name == user_name).first()
    if not usere:
        raise HTTPException(status_code=404, detail="user non trouvé")
    return usere
#methode patch
@router.patch("/usere/{User_id}", response_model=Create_user)
def update_Student(User_id: int, user_update:Create_user, db: Session = Depends(get_db)):
    useres = db.query(User).filter(User.id == User_id).first()
    if not useres:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(useres, key, value)

    db.commit()
    db.refresh(useres)
    return useres
#delete 
@router.delete("/useree/{User_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_Student(User_id: int, db: Session = Depends(get_db)):
    Useres = db.query(User).filter(User.id == User_id).first()
    if not Useres:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    db.delete(Useres)
    db.commit()
