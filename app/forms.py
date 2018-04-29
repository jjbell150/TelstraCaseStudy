
from flask.ext.wtf import Form
from wtforms.fields import TextField, IntegerField, SubmitField
from wtforms.validators import Required

class StoreDocumentForm(Form):
	id = IntegerField('Document ID (int)', validators=[Required()])
	text = TextField('Document Text', validators=[Required()])
	ttl = IntegerField('Time To Live (int)', validators=[Required()])
	submit = SubmitField("Submit document")