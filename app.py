# app.py
from flask import Flask, render_template, request
from models import Department, Course, Professor, Room, TimeSlot

app = Flask(__name__)

# Placeholder data for demonstration purposes
departments = [
    Department('Department A', [Course('Course A1', []), Course('Course A2', ['Course A1'])]),
    Department('Department B', [Course('Course B1', []), Course('Course B2', ['Course B1'])])
]

professors = [Professor('Professor X', ['Monday 9-11', 'Tuesday 13-15']),Professor('Professor Y', ['Wednesday 10-12', 'Thursday 14-16'])]

rooms = [Room('Room 1', 50), Room('Room 2', 40)]

time_slots = [TimeSlot('Monday', '9-11'), TimeSlot('Tuesday', '13-15'),TimeSlot('Wednesday', '10-12'), TimeSlot('Thursday', '14-16')]

# Placeholder timetable (2D list)
timetable = [
    ['Math', 'Physics', 'English', ''],
    ['Chemistry', 'History', '', ''],
    ['', '', 'Biology', 'Computer Science'],
    ['Spanish', '', 'Economics', '']
]

# Function to generate timetable (replace with your actual algorithm)
def generate_timetable(selected_departments):
    # Your timetable generation logic here
    pass

# Routes
@app.route('/')
def index():
    return render_template('index.html', departments=departments)

@app.route('/generate_timetable', methods=['POST'])
def generate_timetable_route():
    # Retrieve data from the form (replace with your frontend structure)
    selected_departments = request.form.getlist('departments[]')

    # Generate timetable (replace with your actual logic)
    generate_timetable(selected_departments)

    # Render the timetable page with generated data
    return render_template('timetable.html', timetable=timetable)

if __name__ == '__main__':
    app.run(debug=True)
