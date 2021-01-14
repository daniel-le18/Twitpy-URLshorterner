from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class urlForm(FlaskForm):
    url = StringField('Original URL', validators=[DataRequired()])
    submit = SubmitField('Shorten')

    def validate_url(self, url):
        if url.data.startswith('https://') is False:
            raise ValidationError(
                'Your link is invalid, please include https://')
