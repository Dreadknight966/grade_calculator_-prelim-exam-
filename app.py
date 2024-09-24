from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route('/calculate',methods=['POST'])
def calculate():

    absence = int(request.form['ATAT'])
    exam = int(request.form['Exam'])
    quiz = int(request.form['Quizgrade1'])
    requirements = int(request.form['Requirements'])
    recitation = int(request.form['Recitation'])

    # attendance_deduction

    if absence == 3:
        att_weight = 30
    elif absence == 2:
        att_weight = 20
    elif absence == 1:
        att_weight = 10
    else:
        att_weight = 0

    quiz1 = quiz * .40
    req = requirements * .30
    rec = recitation * .30

    class_standing = quiz1 + req + rec

    ex = exam * .60
    att = (100 - att_weight) * .10
    clst = class_standing * .30

    Prelim_grade = ex + att + clst

    needed_for_passing = 75 - Prelim_grade
    dean_grade_needed = 90 - Prelim_grade

    if Prelim_grade <= 100 and absence >= 4:
        dean_message = "You have no chance to pass the dean's list :D"
        message = "You have failed due to you're number of absences"
        class_standing = 0
        Prelim_grade = 0
        midterm_pass = 0
        final_pass = 0 
        dean_midterm_pass = 0
        dean_final_pass = 0
    #Passing Grade
    elif Prelim_grade < 50:
        message = "You have a chance to pass!"
        dean_message = "You have no chance to pass the dean's list :D"
        grade_needed = needed_for_passing / (.30 + .50)

        midterm_pass = grade_needed
        final_pass = grade_needed
        dean_midterm_pass = 0
        dean_final_pass = 0

    #Dean's list
    elif Prelim_grade >= 50:
        message = "You have a chance to pass!"
        dean_message = "You have a chance to pass the dean's list :D"
        grade_needed = needed_for_passing / (.30 + .50)

        midterm_pass = grade_needed
        final_pass = grade_needed

        dean_grade = dean_grade_needed / (.30 + .50)
        dean_midterm_pass = dean_grade
        dean_final_pass = dean_grade


    return render_template("index.html", Prelim_grade=Prelim_grade, midterm_pass = midterm_pass, final_pass = final_pass, dean_midterm_pass = dean_midterm_pass, dean_final_pass = dean_final_pass, message = message, dean_message = dean_message)
    
if __name__ == '__main__':
    app.run()
