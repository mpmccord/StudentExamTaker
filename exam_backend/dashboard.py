from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from flask_migrate import current
from .models import db, Course
from .classes_forms import CreateNewClassForm
dashboard = Blueprint("dashboard", __name__)

@dashboard.route('/dashboard')
@login_required
def view_dashboard():
    return render_template("user-dashboard.html")

@dashboard.route('/create', methods=["GET", "POST"])
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

@dashboard.route("/profile/<int:course_id>")
@login_required
def viewCourse(course_id):
    return render_template("view_course.html", current_course=Course.query.get(id == course_id))