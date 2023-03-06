from datetime import datetime
from app import db


class CollectedPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon = db.Column(db.String(40))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def commit(self):
        db.session.add(self)
        db.session.commit()