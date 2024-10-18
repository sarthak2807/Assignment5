from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample quiz questions
quiz = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
    {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Dickens", "Austen"], "answer": "Shakespeare"}
]

@app.route('/')
def home():
    return render_template('quiz.html', quiz=quiz)

@app.route('/submit', methods=['POST'])
def submit():
    answers = request.json.get('answers')
    score = 0
    for i, q in enumerate(quiz):
        if answers.get(str(i)) == q["answer"]:
            score += 1
    return jsonify({"score": score, "total": len(quiz)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

