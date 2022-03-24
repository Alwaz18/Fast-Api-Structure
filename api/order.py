from sqlalchemy.orm import Session
from schema import schemas
from models import models
from fastapi import HTTPException, status


def get_all(db: Session):
    orders = db.query(models.Order).all()
    return orders


def create(request: schemas.Order, db: Session):
    new_order = models.Order(title=request.title, body=request.body, user_id=1)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


def destroy(id: int, db: Session):
    order_to_delete = db.query(models.Order).filter(models.Order.id == id)

    if not order_to_delete.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with id {id} not found.")
    order_to_delete.delete(synchronize_session=False)
    db.commit()
    return {'done'}


def update(id: int, request: schemas.order, db: Session):
    order = db.query(models.Order).filter(models.Order.id == id)
    if not order.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with id {id} not found")
    order.update(request.__dict__)
    db.commit()
    return 'updated'


def show(id: int, db: Session):
    order = db.query(models.Order).filter(models.Order.id == id).first()
    if order:
        return order
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with the id {id} is not available")
