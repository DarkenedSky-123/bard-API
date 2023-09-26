from flask import Flask, request, jsonify
from bardapi import Bard

app = Flask(__name__)

# Replace 'your_token_here' with your actual Bard API token


@app.route('/ask', methods=['GET'])
def ask_question():
    TOKEN = 'bAgzQ7Qp_J0SSTQw6nFTsf8q9QQeKFjKMLmHiSccyMmLJxYg3SwPyC98ziSAzjql-jGgbw.'
    bard = Bard(token=TOKEN)
    try:
        question = request.args.get('question')
        if question:
            response = bard.get_answer(question)
            answer = response['content']
            return jsonify({'answer': answer})
        else:
            return jsonify({'error': 'Invalid input. Please provide a question as a query parameter.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)