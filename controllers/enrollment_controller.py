from flask import Blueprint, jsonify
from models import db
from models.enrollment import Enrollment
from sqlalchemy.orm import joinedload

enrollment_bp = Blueprint('enrollment', __name__)

@enrollment_bp.route('/enrollments', methods=['GET'])
def get_enrollments():
    try:
        enrollments = Enrollment.query.options(joinedload(Enrollment.student), joinedload(Enrollment.course)).all()

        if not enrollments:
            return jsonify({'message': 'No enrollments found'}), 404

        result = []
        for enrollment in enrollments:
            result.append({
                'id': enrollment.id,
                'student_name': enrollment.student.name,  # Mengambil nama student
                'course_name': enrollment.course.mata_kuliah,  # Mengganti 'name' dengan 'mata_kuliah'
                'course_id': enrollment.course_id,
                'student_id': enrollment.student_id
            })

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500