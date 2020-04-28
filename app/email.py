from threading impor Thread
from flask_mail import Message
from flask import current_app, render_template

#from . import mail

def send_async_mail(message):
    #with app.app_context():
    #mail.send(message)
    pass

def welcome_mail(user):
    message = Message('Bienvenido!',
                        sender=current_app.config['MAIL_USERNAME'],
                        recipients=[user.email])
    message.html = render_template('email/welcome.hmtl', user=user)
    thread = Thread(target=send_async_mail, args=[message])
    thread.start()
