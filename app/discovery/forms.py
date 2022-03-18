from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    """
    Given class is a form class model for search fund
    """

    search = StringField("Search fund", validators=[DataRequired()])
