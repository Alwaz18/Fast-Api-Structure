# from enum import unique
from database.configuration import Base
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String, nullable=True)
    order_address = Column(String)
    information = Column(JSON, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="orders")
    # addresses = relationship("Orders", back_populates="creator")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    address = Column(String)
    orders = relationship("Orders", back_populates="creator")


# ou can query column properties of mapped classes and the Query class has a generative distinct() method:

# for value in Session.query(Table.column).distinct():
#      pass
# #
