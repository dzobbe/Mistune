from flask import request, render_template, flash, send_from_directory, abort
from ctfapp import db, app
from .forms import TextFormTest, TextFormSend
from .model import Mdowndb
import mistune


renderer = mistune.Renderer(escape=True, hard_wrap=True)
markdown = mistune.Markdown(renderer=renderer)


@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt')


@app.route('/', methods=['GET', 'POST'])
@app.route('/tester', methods=['GET', 'POST'])
def test():
    form = TextFormTest(request.form)
    if form.validate_on_submit():
        return render_template('test.html', form=form, html=markdown(form.text.data))
    return render_template('test.html', form=form, html='')


@app.route('/send', methods=['GET', 'POST'])
def send():
    form = TextFormSend(request.form)
    if form.validate_on_submit():
        mdown = Mdowndb(form.text.data)
        db.session.add(mdown)
        db.session.commit()
        flash('Thank you. The admin will have a look soon!')
    return render_template('send.html', form=form)


@app.route('/queue')
def queue():
    num = Mdowndb.query.filter(Mdowndb.visited==False).count()
    return str(num) + ' still in queue', 200



@app.route('/checkit')
def checkit():
    if request.remote_addr != app.config['ADDR']:
        dbitem = Mdowndb.query.filter(Mdowndb.visited==False).first()
        if dbitem:
            dbitem.visited = True
            db.session.commit()
            return markdown(dbitem.text)
        else:
            return 'non found'
    else:
        return abort(404)


@app.route('/nothingherewhyareyoulookinghere')
def goof():
    return 'well it is a web challenge', 200
