# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitFieldfrom wtforms.validators import DataRequired, Length

class ItemForm(FlaskForm):
    name = StringField(
        "Nom",
        validators=[DataRequired(), Length(max=80)]
    )
    description = TextAreaField("Description")
    submit = SubmitField("Enregistrer")