from flask import Blueprint, render_template, flash, redirect, url_for
from flask.ext.mail import Message
from booa.main.forms import ContactForm

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def home():
    return render_template("home.html", tab="home")


@main.route('/vision')
def vision():
    return render_template("vision.html", tab="vision")

@main.route('/background')
def background():
    return render_template("background.html", tab="background")

@main.route('/projects')
def projects():
    return render_template("projects.html", tab="projects")

@main.route('/team')
def team():
    return render_template("team.html", tab="team")

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        from booa.booa_app import mail
        msg = Message("Contact request", sender="brasouvertsopenarms@gmail.com",
                      recipients=["chris.moirano@gmail.com"])
        # mail.send(msg)
        flash('Thank you, we will respond to your message as soon as possible')
        return redirect(url_for('main.contact'))
    ctx = {"tab": "contact", "form": form}
    return render_template("contact.html", **ctx)

@main.route('/contribute')
def contribute():
    return render_template("contribute.html", tab="contribute")
