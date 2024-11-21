from sqlalchemy import Column, Integer, String, Float, Boolean
from backend.database import Base

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    category = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    manufacturer = Column(String)
    expiry_date = Column(String)
    prescription_required = Column(Boolean)
    discount_percentage = Column(Float)
