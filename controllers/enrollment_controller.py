from flask import Blueprint, jsonify, request
from models.enrollment import Enrollment, db
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError

# Membuat blueprint untuk enrollments
enrollment_bp = Blueprint('enrollment', __name__)

# Metode GET untuk mendapatkan semua enrollments
@enrollment_bp.route('/enrollments', methods=['GET'])
def get_enrollments():
    try:
        enrollments = Enrollment.query.options(
            joinedload(Enrollment.student),
            joinedload(Enrollment.course)
        ).all()

        if not enrollments:
            return jsonify({'message': 'No enrollments found'}), 404

        result = []
        for enrollment in enrollments:
            result.append({
                'id': enrollment.id,
                'student_name': enrollment.student.name,
                'course_name': enrollment.course.mata_kuliah,
                'course_id': enrollment.course_id,
                'student_id': enrollment.student_id
            })

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

# Metode POST untuk membuat enrollment baru
@enrollment_bp.route('/enrollments', methods=['POST'])
def create_enrollment():
    try:
        data = request.get_json()
        student_id = data.get('student_id')
        course_id = data.get('course_id')

        if not student_id or not course_id:
            return jsonify({'message': 'student_id and course_id are required'}), 400

        new_enrollment = Enrollment(student_id=student_id, course_id=course_id)
        db.session.add(new_enrollment)
        db.session.commit()

        return jsonify({'message': 'Enrollment created successfully', 'id': new_enrollment.id}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Student or Course not found'}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

# Metode PUT untuk memperbarui enrollment berdasarkan ID
@enrollment_bp.route('/enrollments/<int:id>', methods=['PUT'])
def update_enrollment(id):
    try:
        enrollment = Enrollment.query.get(id)
        if not enrollment:
            return jsonify({'message': 'Enrollment not found'}), 404

        data = request.get_json()
        student_id = data.get('student_id')
        course_id = data.get('course_id')

        if student_id is not None:
            enrollment.student_id = student_id
        if course_id is not None:
            enrollment.course_id = course_id

        db.session.commit()
        return jsonify({'message': 'Enrollment updated successfully'}), 200

    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Student or Course not found'}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

# Metode DELETE untuk menghapus enrollment berdasarkan ID
@enrollment_bp.route('/enrollments/<int:id>', methods=['DELETE'])
def delete_enrollment(id):
    try:
        enrollment = Enrollment.query.get(id)
        if not enrollment:
            return jsonify({'message': 'Enrollment not found'}), 404

        db.session.delete(enrollment)
        db.session.commit()
        return jsonify({'message': 'Enrollment deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500
