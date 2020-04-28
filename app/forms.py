from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField
from werkzeug.security import generate_password_hash

from .models import User

def codi_validator(form,field):
    if field.data == 'codi' or field.data == 'Codi':
        raise validators.ValidationError('El username codi no es permitido.')

class LoginForm(Form):
    username = StringField('Usuario',[
        validators.length(min=4, max=50)
    ])
    password = PasswordField('Password',[
        validators.Required()
    ])

class RegisterForm(Form):
    username = StringField('Usuario',[
        validators.length(min=4, max=50),
        validators.Required(),
        codi_validator
    ])
    email = EmailField('Correo electrónico',[
        validators.length(min=6, max=100),
        validators.Required(message='El email es requerido'),
        validators.Email(message='Ingrese un email válido')
    ])
    password = PasswordField('Password',[
        validators.Required()
    ])
    confirm_password = PasswordField('Repeat Password',[
        validators.EqualTo('confirm_password')
    ])
    accept = BooleanField('',[
        validators.DataRequired()
    ])

    def validate_username(self, field):
        if User.get_by_username(field.data):
            raise validators.ValidationError('El Username ya esta siendo usado')

    def validate_email(self, field):
        if User.get_by_username(field.data):
            raise validators.ValidationError('El email ya esta siendo usado')

class TaskForm(Form):
    title = StringField('Título',[
        validators.length(min=4, max=50, message='Título fuera de rango'),
        validators.DataRequired(message='El título es requerido.')
    ])
    description = TextAreaField('Descripción',[
        validators.DataRequired(message='La Descripción es requerida.')
    ],render_kw={'rows':5})
