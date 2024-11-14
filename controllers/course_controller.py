from flask import Blueprint, request, jsonify
from models.course import Course, db

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()

    # Validasi input
    if 'mata_kuliah' not in data or not data['mata_kuliah']:
        return jsonify({'error': 'Mata kuliah is required'}), 400

    new_course = Course(mata_kuliah=data['mata_kuliah'])  # Menggunakan 'mata_kuliah' sesuai model

    try:
        db.session.add(new_course)
        db.session.commit()
        return jsonify({'message': 'Course created', 'course_id': new_course.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create course', 'message': str(e)}), 500

@course_bp.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{'id': course.id, 'mata_kuliah': course.mata_kuliah} for course in courses]), 200  # Menggunakan 'mata_kuliah' sesuai model