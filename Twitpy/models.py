from datetime import datetime
from Twitpy import db
import string
from random import choices


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512), nullable=False)
    shorten_url = db.Column(db.String(5), unique=True, nullable=False)
    date_created = db.Column(db.DateTime,
                             nullable=False,
                             default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shorten_url = self.generate_short()

    def generate_short(self):
        character_basket = string.digits + string.ascii_letters
        shorten_url = ''.join(choices(character_basket, k=5))

        link = self.query.filter_by(shorten_url=shorten_url).first()
        if link:
            return self.generate_short()
        else:
            return shorten_url

    def __repr__(self) -> str:
        return f"URL('{self.original_url}','{self.shorten_url}')"