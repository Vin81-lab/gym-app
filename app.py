from flask import Flask
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Create database
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Database connected successfully!"

from flask import render_template, request, redirect, url_for
from models import Member
@app.route('/members', methods=['GET', 'POST'])
def members():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        plan = request.form['plan']

        new_member = Member(name=name, age=age, plan=plan)
        db.session.add(new_member)
        db.session.commit()

        return redirect(url_for('members'))

    all_members = Member.query.all()
    return render_template('members.html', members=all_members)
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_member(id):
    member = Member.query.get_or_404(id)

    if request.method == 'POST':
        member.name = request.form['name']
        member.age = request.form['age']
        member.plan = request.form['plan']

        db.session.commit()
        return redirect(url_for('members'))

    return render_template('edit_member.html', member=member)
@app.route('/delete/<int:id>')
def delete_member(id):
    member = Member.query.get_or_404(id)

    db.session.delete(member)
    db.session.commit()

    return redirect(url_for('members'))

if __name__ == '__main__':
    app.run(debug=True)
