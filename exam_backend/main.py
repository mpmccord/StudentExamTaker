# main.py

from flask import Blueprint, render_template, redirect, request, url_for, g, flash
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
@main.route("/profile/<int:course_id>")
@login_required
def view_course(course_id):
    selected_course = Course.query.get(course_id)
    if selected_course.teacher != current_user.id:
        flash("You are not authorized to view this resource")
        return redirect(url_for("main.profile"))
    return render_template("view_course.html", selected_course = selected_course, courses=current_user.courses)

@main.route("/create-exam/<int:course_id>", methods = ['POST', 'GET'])
@login_required
def createExam(course_id):
    form = CreateNewExamForm()
    if request.method == 'POST':
        exam_name = request.form.get("name")
        my_exam = Exam()
    return render_template("adding_new_courses.html", form = form)


def get_exam(post_id):
    exam = Exam.query.filter_by(teacher=current_user.id, id=post_id).first()
    if not exam:
        flash("Invalid exam")
        return redirect(url_for("main.profile"))
