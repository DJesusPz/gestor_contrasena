from flask import Flask
from flask_cors import CORS
from flask import jsonify,request
import pymysql

app=Flask(__name__)
## Nos permite acceder desde una api externa
CORS(app)
## Funcion para conectarnos a la base de datos de mysql
def conectar(vhost,vuser,vpass,vdb):
    conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset = 'utf8mb4')
    return conn
# Ruta para consulta general del baul de contraseñas
@app.route("/")
def consulta_general():
    try:
        conn=conectar('localhost','root','','gestor_contrasena')
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM baul """)
        datos=cur.fetchall()
        data=[]
        for row in datos:
            dato={'id_baul':row[0],'plataforma':row[1],'usuario':row[2],'clave':row[3]}
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify({'baul':data,'mensaje':'Baul de contraseñas'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})

@app.route("/consulta_individual/<codigo>",methods=['GET'])
def consulta_individual(codigo):
    try:
        conn=conectar('localhost','root','','gestor_contrasena')
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM baul where id_baul='{0}' """.format(codigo))
        datos=cur.fetchall()
        cur.close()
        conn.close()
        if datos!=None:
            dato={'id_baul':datos[0],'Plataforma':datos[1],'usuario':datos[2],'clave':datos[3]}
            return jsonify({'mensaje':'Registro no encontrado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
    
def encriptar_sql(password):
    conn = pymysql.connect(host='localhost', user='root', password='', db='gestor_contrasena')
    cur = conn.cursor()
    cur.execute("SELECT AES_ENCRYPT(%s, 'tu_clave_de_encriptacion')", (password,))
    encripted_password = cur.fetchone()[0]
    cur.close()
    conn.close()
    return encripted_password

# Modificar la función registro para encriptar la contraseña antes de guardarla en la base de datos
@app.route("/registro/", methods=['POST'])
def registro():
    try:
        conn = conectar('localhost', 'root', '', 'gestor_contrasena')
        cur = conn.cursor()
        
        # Encriptar la contraseña antes de guardarla en la base de datos
        encripted_clave = encriptar_sql(request.json['clave'])
        
        cur.execute("INSERT INTO baul (Plataforma, usuario, clave) VALUES (%s, %s, %s)", 
                    (request.json['Plataforma'], request.json['usuario'], encripted_clave))
        
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({'mensaje': 'Registro agregado exitosamente'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    
@app.route("/eliminar/<codigo>",methods=['DELETE'])
def eliminar(codigo):
    try: 
        conn=conectar('localhost','root','','gestor_contrasena')
        cur = conn.cursor()
        x=cur.execute(""" delete from baul where id_baul={0}""".format(codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
    
@app.route("/actualizar/<codigo>",methods=['PUT'])
def actualizar(codigo):
    try:
        conn=conectar('localhost','root','','gestor_contrasena')
        cur = conn.cursor()
        x=cur.execute(""" update baul set Plataforma='{0}',usuario='{1}',clave='{2}' where \
            id_baul={3}""".format(request.json['Plataforma'],request.json['usuario'],request.json['clave'],codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'}) 
if __name__=='__main__':
    app.run(debug=True)
