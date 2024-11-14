from sqlalchemy import Column, Integer, String
from models import db
from sqlalchemy.orm import relationship

class Student(db.Model):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    # Relasi
    enrollments = relationship('Enrollment', back_populates='student')