from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL


class AddPetForm(FlaskForm):
    """Form to add a pet"""

    name = StringField('Name', validators = [InputRequired()])
    species = SelectField ('Species', 
                            choices= [('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField('photo_url', validators = [Optional(), URL()])
    age = IntegerField ('age', validators = [Optional(), NumberRange(min=0, max=30, message = 'Age has to be between 0 and 30')])
    notes = TextAreaField ('notes', validators = [Optional()])

class EditPetForm(FlaskForm):
    """Form to edit a pet"""
    
    photo_url = StringField('photo_url', validators = [Optional(), URL()])
    notes = TextAreaField ('notes', validators = [Optional()])
    available = BooleanField('available')
