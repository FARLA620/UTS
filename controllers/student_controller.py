from flask import Blueprint, jsonify, request
from models import db
from models.student import Student

student_bp = Blueprint('student', __name__)

@student_bp.route('/mahasiswa', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students])

@student_bp.route('/mahasiswa', methods=['POST'])
def add_student():
    data = request.get_json()  # Menggunakan get_json untuk parsing

    # Validasi input
    if 'name' not in data or not data['name']:
        return jsonify({'error': 'Name is required'}), 400

    new_student = Student(name=data['name'])

    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'id': new_student.id, 'name': new_student.name}), 201
    except Exception as e:
        db.session.rollback()  # Rollback jika terjadi kesalahan
        return jsonify({'error': 'Failed to add student', 'message': str(e)}), 500