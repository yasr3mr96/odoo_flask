from wtforms import Form, StringField,PasswordField,TextAreaField,validators,IntegerField




class Product(Form):
	name=StringField("Name",[validators.Length(min=4,max=40)])
	cost=IntegerField("Sales Price")


