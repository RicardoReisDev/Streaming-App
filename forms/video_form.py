from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class VideoForm(FlaskForm):
    title = StringField('Título do Vídeo')
    url = StringField('URL do Vídeo')
    submit = SubmitField('Adicionar Vídeo')
