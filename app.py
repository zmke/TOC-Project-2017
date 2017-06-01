# encoding: utf-8
import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

first = 0

API_TOKEN = '387203602:AAEU7r1xS2Wpl4StrRX9G0vtDbc16q0U8Z8'
WEBHOOK_URL = 'https://e72af5c3.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'start',
        'shoulder',
        'upper',
        'lower',
        's_1',
        's_2',
        's_2_1',
        's_2_2',
        's_3',
        'u_1',
        'u_2',
        'u_3',
        'l_1',
        'l_2',
        'l_3'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'start',
            'conditions': 'start_chosen'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'shoulder',
            'conditions': 'shoulder_chosen'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'upper',
            'conditions': 'upper_chosen'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'lower',
            'conditions': 'lower_chosen'
        },
        {
            'trigger': 'advance',
            'source': 'shoulder',
            'dest': 's_1',
            'conditions': 's_1_chosen'
        },
        {
            'trigger': 'advance',
            'source': 'shoulder',
            'dest': 's_2',
            'conditions': 's_2_chosen'
        },
        {
            'trigger': 'advance',
            'source': 's_2',
            'dest': 's_2_1',
            'conditions': 's_2_1_chosen'
        },
        {
            'trigger': 'advance',
            'source': 's_2',
            'dest': 's_2_2',
            'conditions': 's_2_2_chosen'
        },
        {
            'trigger': 'advance',
            'source': 'shoulder',
            'dest': 's_3',
            'conditions': 's_3_chosen'
        },
        {
            'trigger': 'advance',
            'source': 'upper',
            'dest': 'u_1',
            'conditions': 'u_1_chosen'
        },
        {
            'trigger': 'advance',
            'source': 'upper',
            'dest': 'u_2',
            'conditions': 'u_2_chosen'
        },
        {
            'trigger': 'advance',
            'source': 'upper',
            'dest': 'u_3',
            'conditions': 'u_3_chosen'
        },
        {
            'trigger': 'advance',
            'source': 'lower',
            'dest': 'l_1',
            'conditions': 'l_1_chosen'
        },
        {
            'trigger': 'advance',
            'source': 'lower',
            'dest': 'l_2',
            'conditions': 'l_2_chosen'
        },
        {
            'trigger': 'advance',
            'source': 'lower',
            'dest': 'l_3',
            'conditions': 'l_3_chosen'
        },
        {
            'trigger': 'go_back',
            'source': [
                'start',
                's_1',
                's_2_1',
                's_2_2',
                's_3',
                'u_1',
                'u_2',
                'u_3',
                'l_1',
                'l_2',
                'l_3',
                'upper',
                'lower'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    global first
    if first == 0:
        first = 1
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
