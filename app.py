from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from syndrum import ask, append_interation_to_chat_log

app = Flask(__name__)

app.config['SECRET_KEY'] = '89djh9lhkd93'

@app.route('/syndrum', methods=['POST'])
def syndrum():
    incoming_msg = request.values['body']
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interation_to_chat_log(incoming_msg, answer,
                                                         chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)

if __name__ == '__main__':
    app.run(debug=True)