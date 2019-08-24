#___________________________________________________________________________________________________________________________
#_________________________________________Import Libraries_________________________________________________________________
from flask import Flask,render_template,redirect,request,session,url_for,flash
from forms import *
from odoo_api import OdooApi
#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________




#_________________________________________________init app__________________________________________________________________
#___________________________________________________________________________________________________________________________
app=Flask(__name__)
api=OdooApi('http://0.0.0.0:8012','pos','yasser','1')
#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________






#__________________________________________________________Home Page_________________________________________________________________
#___________________________________________________________________________________________________________________________
@app.route('/')
def index():
	return render_template('home.html')
#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________






#__________________________________________________________________Create Article Page _________________________________________________________
#___________________________________________________________________________________________________________________________
@app.route("/create",methods=["GET","POST"])
def create():
	frm=Product(request.form)
	if request.method=="POST" and frm.validate():
		name=frm.name.data
		cost=frm.cost.data
		api.create('product.template', [{'name': name,'list_price':cost}])
		flash('Article has been published successfully!', 'success')
		return redirect(url_for("showallproducts"))
	return render_template("add_product.html",form=frm)
#___________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________








#__________________________________________________________________show all Products_________________________________________________________
#___________________________________________________________________________________________________________________________
@app.route("/products")
def showallproducts():
	products=api.search2('product.template', [[['list_price', '>', '100']]],['name'])
	print(products)
	if products:
		print(products)
		return render_template("products.html",data=products)
	else:
		msg = "No product found"
		return render_template("products.html",msg=msg)

#_______________________________________________________________main____________________________________________________________

if __name__=="__main__":
	app.secret_key = '@%^&(*9867ahsh)'
	app.run(debug=True)

#___________________________________________________________________________________________________________________________
