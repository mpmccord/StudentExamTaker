from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from flask_login import login_required
from .models import db, Course
dashboard = Blueprint("dashboard", __name__)

@dashboard.route('/dashboard')
@login_required
def view_dashboard():
    return render_template("user-dashboard")

@dashboard.route("/add_course")
@login_required
def add_new_course():
    name = request.form.get("name")
    course = Course(name=name, teacher = g.user, school = g.school)
    db.add(course)
    db.commit()