# main.py

from flask import Blueprint, render_template, redirect, request, url_for, g
from flask_login import login_required, current_user
from .classes_forms import CreateNewClassForm, CreateNewExamForm
from .models import db, Course, Exam
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    email = current_user.email
    courses = current_user.courses
    return render_template('user-dashboard.html', email=email, courses=courses) #courses=current_user.courses)

@main.route('/create', methods=["GET", "POST"])
@login_required
def add_new_course():
    form = CreateNewClassForm()
    if request.method == 'POST':
        course_name = request.form.get("name")
        course = Course(name=course_name, teacher=current_user.id)
        
        # new_user.courses = [course.id]

        # add the new course to the database
        db.session.add(course)
        db.session.commit()

        return redirect(url_for('main.profile', courses=current_user.courses))
    else:
        return render_template("adding_new_courses.html", form=form)

@main.route("/create-exam/<int:course_id>", methods = ['POST', 'GET'])
def createExam(course_id):
    form = CreateNewExamForm()
    if request.method == 'POST':
        exam_name = request.form.get("name")
        my_exam = Exam()
    return render_template("adding_new_courses.html", form = form)
