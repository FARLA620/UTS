from sqlalchemy import Column, Integer, ForeignKey
from models import db
from sqlalchemy.orm import relationship

class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    # Relasi
    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')