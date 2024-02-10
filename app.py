from flask import Flask, render_template, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
from forms.video_form import VideoForm

app = Flask(__name__)
app.config.from_pyfile('instance/config.py')  
db = SQLAlchemy(app)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Video('{self.title}', '{self.url}')"

def create_app():
    with app.app_context():
        db.create_all()  
    return app

@app.route('/', methods=['GET', 'POST'])
def home():
    videos = Video.query.all()
    form = VideoForm()

    if form.validate_on_submit():
        new_video = Video(title=form.title.data, url=form.url.data)
        db.session.add(new_video)
        db.session.commit()

        # Redirecionamento após a inserção do vídeo
        return redirect(url_for('home'))

    response = make_response(render_template('home.html', videos=videos, form=form))
    response.set_cookie('my_cookie', 'cookie_value', secure=True, samesite='None') 
    return response

if __name__ == '__main__':
    create_app().run(debug=True)
