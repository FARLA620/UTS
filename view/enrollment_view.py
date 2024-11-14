from flask import jsonify
from models.enrollment import Enrollment

def get_all_enrollments():
    enrollments = Enrollment.query.all()
    return jsonify([{'id': enrollment.id, 'student_id': enrollment.student_id, 'course_id': enrollment.course_id} for enrollment in enrollments])