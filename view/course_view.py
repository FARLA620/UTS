from flask import jsonify
from models.course import Course

def get_all_courses():
    courses = Course.query.all()
    return jsonify([{'id': course.id, 'title': course.title} for course in courses])