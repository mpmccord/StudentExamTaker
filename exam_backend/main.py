# main.py

from flask import Blueprint, render_template, redirect, request, url_for, g, flash
from flask_login import login_required, current_user
from .classes_forms import CreateNewClassForm, CreateNewExamForm, AddQuestionForm
from .models import db, Course, Exam, Question
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
        if not Course.query.get(course_id) or Course.query.get(course_id).teacher != current_user.id:
            flash("Invalid user")
            return redirect(url_for("main.profile"))
        exam_name = request.form.get("name")
        my_exam = Exam(name=exam_name, course_class=course_id, school=current_user.school)
        db.session.add(my_exam)
        db.session.commit()
        return redirect(url_for("main.view_course", course_id=course_id))
    return render_template("create_new_exam.html", form = form, course_name = Course.query.get(course_id).name)

@main.route("/profile/view_exam/<int:exam_id>")
@login_required
def get_exam(exam_id):
    exam = Exam.query.get(exam_id)
    if not exam or Course.query.get(exam.course_class).teacher != current_user.id:
        flash("Invalid exam")
        return redirect(url_for("main.profile"))
    return render_template("view_exam.html", selected_course = Course.query.get(exam.course_class), courses=current_user.courses, selected_exam=exam)

@main.route("/profile/update_exam", methods = ["GET", "POST"])
@login_required
def setQuestions(exam_id):
    exam = Exam.query.get(exam_id)
    if not exam or Course.query.get(exam.course_class).teacher != current_user.id:
        flash("Unauthorized resource")
        return redirect(url_for("main.profile"))
    form = AddQuestionForm()
    if request.method == "POST":
        text = request.form.get("text")
        # The three possible answers that the user can choose.
        a = request.form.get("a")
        b = request.form.get("b")
        c = request.form.get("c")
        # Possible correct answers
        choices = ["a", "b", "c"]
        correct_answer = request.form.get("c")

@main.route("/test", methods=("GET", "POST"))
def test():
    form = AddQuestionForm()
    if request.method == "POST":
        text = request.form.get("text")
        # answer_response = request.form.get("possible_answers")
        print(text)
        quest = Question(text_question = text, answers = ["None"], given_exam=1)
        print(text)
        db.session.add(quest)
        db.session.commit()
        flash("You have successfully added a question!")
        return redirect(url_for("main.index"))
    return render_template("add_new_question.html", form=form)