from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)


ques = [
    "1. What is an exception in Java?",
    "2. Which keyword is used to handle exceptions in Java?",
    "3. What is the purpose of the 'finally' block in exception handling?",
    "4. Which of the following is NOT a type of exception in Java?",
    "5. What will happen if an exception occurs in a try block and there is no corresponding catch block?",
    "6. What is the superclass of all exception classes in Java?",
    "7. Which keyword is used to manually throw an exception in Java?",
    "8. What is the purpose of the 'throws' keyword in Java?",
    "9. Which of the following statements about checked exceptions is true?",
    "10. How can you handle multiple exceptions in a single try block?"
]

options = [
    ["A) A syntax error", "B) An event that occurs during the execution of a program that disrupts the normal flow of instructions", "C) A warning message", "D) A type of loop"],
    ["A) try", "B) catch", "C) throw", "D) All of the above"],
    ["A) It is used to catch exceptions.", "B) It is used to specify code that will always be executed, regardless of whether an exception occurs.",
        "C) It is used to throw exceptions.", "D) It is used to define custom exceptions."],
    ["A) Checked exceptions", "B) Unchecked exceptions", "C) Runtime exceptions", "D) Unhandled exceptions"],
    ["A) The program will terminate.", "B) The exception will be ignored.", "C) The finally block will be executed.", "D) The program will continue execution normally."],
    ["A) Throwable", "B) Exception"],
    ["A) try", "B) catch", "C) throw", "D) finally"],
    ["A) To declare checked exceptions that a method might throw", "B) To catch exceptions", "C) To define custom exceptions", "D) To handle exceptions within a method"],
    ["A) They are checked at compile-time.", "B) They are optional to handle.", "C) They are subclasses of RuntimeException.", "D) They are always fatal and cannot be recovered from."],
    ["A) By using multiple catch blocks", "B) By separating exceptions with commas in a single catch block",
        "C) By using if-else statements within a catch block", "D) By using nested try-catch blocks"]
]

correct_answers = ['B', 'D', 'B', 'D', 'A', 'A', 'C', 'A', 'A', 'A']


@app.route('/')
def index():
    return render_template('quiz.html', ques=ques, options=options)


@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    recieved_answers = [request.form.get(f'q{i}') for i in range(0, 10)]
    user_answers=[chr(ord('A')+int(i)-1) for i in recieved_answers]
    print(user_answers)
    score = sum(1 for myAns, Ans in zip(user_answers, correct_answers) if myAns == Ans)
    print(score)
    max_score = len(ques)
    result = {}
    if score == max_score:
        result['message'] = f"EXCELLENT, You scored full marks ({score}/{max_score})"
    elif score >= 0.7 * max_score:
        result['message'] = f"Congratulations! You passed with score of {score}/{max_score}"
    elif score <= 0.25 * max_score:
        result['message'] = f"Very poor performance needs improvement ({score}/{max_score})"
    else:
        result['message'] = f"You unfortunately failed with score of {score}/{max_score}"
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
    
