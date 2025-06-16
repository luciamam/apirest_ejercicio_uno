from flask import Flask,jsonify,render_template,request
from pymongo import MongoClient
from Productos.productos import productoslista
from bson import ObjectId




app=Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
#client=MongoClient("mongodb+srv://lucia:12345@despliegueflask.vlrjgyf.mongodb.net/")
db=client['Apirest']
productos=db["productos"]



@app.route('/anydar',methods=['POST'])
def anydarproducto():

    return "poducto"
    




@app.route('/')
def home():
    #productos.insert_many(productoslista)
    return jsonify(productoslista)
    





@app.route('/admin')
def inerstarproductos():
    return render_template ("PanelAdministrador.html")


# @app.route('/crear')
# def anydarproductos():
#     productos.insert_many(productoslista)
#     return "productos añadidos"

# @app.route('/anydarproducto' ,methods=['GET','POST'])
# def addproducto():
#     if request.method=='POST':
#         datos=request.form
#         nombre=datos["nombre"]
#         precio=datos["precio"]
#         cantidad=datos["cantidad"]
#         estado=datos["estado"]
#         producto={
#             "nombre":nombre,
#             "precio":precio,
#             "cantidad":cantidad,
#             "estado":estado

#         }
#         productos.insert_one(producto)
#         return  "producto añadidio"

#     else:
#         return render_template('Addproducto.html')





# @addproducto('/ediatproducto/<id>',methods=['GET','POST']) 
# def editar(id):
#     if request.method=='POST':
#         datos=request.form
#         producto=productos.find_one({"_id":ObjectId(id)})
#         productos.update_one({"_id":producto["_id"]},{"$set":{"precio":datos["precio"]}})
#         return "peoducto actualizado "
#     else:
#         render_template("Editarproducto.html")

    



if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")