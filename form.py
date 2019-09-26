#!/usr/bin/python3.7
# UTF8
# Date: Fri 16 Aug 2019 15:39:17 CEST
# Author: Nicolas Flandrois
# Requirement for this section: pip install flask-wtf

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class QuestionForm(FlaskForm):
    message = StringField('Entrez votre message',
                           validators=[DataRequired(), Length(min=2, max=20)])

    submit = SubmitField('Envoyer')
