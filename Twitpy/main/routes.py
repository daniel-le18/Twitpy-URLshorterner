from Twitpy.main.forms import urlForm
from flask import render_template, Blueprint, redirect
from Twitpy.models import URL
from Twitpy import db
main = Blueprint('main', __name__)


@main.route('/<short_url>')
def redirect_to(short_url):
    link = URL.query.filter_by(shorten_url=short_url).first_or_404()
    return redirect(link.original_url)


# Main page
@main.route("/", methods=['GET', 'POST'])
def home():
    form = urlForm()
    if form.validate_on_submit():
        link = URL(original_url=form.url.data)
        db.session.add(link)
        db.session.commit()
        return render_template("home.html", form=form, new=link.shorten_url)
    return render_template("home.html", form=form)
