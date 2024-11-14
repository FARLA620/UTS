from flask import jsonify
from models.student import Student

def get_all_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students])