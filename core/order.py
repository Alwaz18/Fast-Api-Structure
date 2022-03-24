from schema.oa2 import get_current_user
from fastapi import APIRouter, Depends, status, Response
from schema import schemas
from database import configuration
from typing import List
from sqlalchemy.orm import Session
from api import order

router = APIRouter(tags=["Orders"], prefix="/order")
get_db = configuration.get_db


@router.get("/", response_model=List[schemas.ShowOrder])
def get_all_orders(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return order.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Order, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return order.create(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowOrder)
def get_order_by_id(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return order.show(id, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return order.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_order(id: int, request: schemas.Order, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return order.update(id, request, db)
