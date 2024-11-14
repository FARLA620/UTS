from sqlalchemy import Column, Integer, String
from models import db
from sqlalchemy.orm import relationship

class Course(db.Model):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    mata_kuliah = Column(String(100), nullable=False)  # Mengganti 'name' dengan 'mata_kuliah'

    # Relasi
    enrollments = relationship('Enrollment', back_populates='course')