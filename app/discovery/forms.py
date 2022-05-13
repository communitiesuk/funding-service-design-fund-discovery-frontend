from flask_wtf import FlaskForm
from wtforms import EmailField
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import Email


class SearchForm(FlaskForm):
    """
    Given class is a form class model for search fund
    """
    search = StringField("Search fund", validators=[DataRequired()])


class EmailForm(FlaskForm):
    """EmailForm This class contains the logic for the email form.

    A FlaskForm combined with some logic for handling the email address
    submission.
    """
    email = EmailField("email field", validators=[Email()])
