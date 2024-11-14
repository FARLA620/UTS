from flask import Flask, jsonify
from config import Config
from models import db
from flask_migrate import Migrate
from controllers.student_controller import student_bp
from controllers.enrollment_controller import enrollment_bp
from controllers.course_controller import course_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()  


app.register_blueprint(student_bp)
app.register_blueprint(enrollment_bp)
app.register_blueprint(course_bp)
@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"Error occurred: {str(e)}")
    
    return jsonify({'error': 'An error occurred', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
