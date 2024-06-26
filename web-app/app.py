from flask import Flask, request, jsonify, render_template
import openai

app=Flask(__name__)

openai.api_key='.txt'

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