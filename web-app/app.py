from flask import Flask, request, jsonify, render_template
import opentracing

app=Flask(__Proyecto__)

openai.api_key='sk-proj-IWNvr9t9p6YEgRGNOBjGT3BlbkFJLOY8F05879EQv5lWzVsU'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": user_message}
        ]
    )
    return jsonify(response.choices[0].message['content'])


if __name__ == '__main__':
    app.run(debug=True)