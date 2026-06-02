# app/models.py
from . import db

class Item(db.Model):
    """Simple modèle « Item » avec un nom et une description."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Item {self.id}: {self.name}>"