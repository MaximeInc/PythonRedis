from flask import Flask,request,jsonify,redirect,url_for
import redis

#Création de la connexion au serveur Redis
my_reddis = redis.Redis(
    host='127.0.0.1',
    port=6379, 
    password='')

#Purge de la base
my_reddis.flushdb()

#Initialisation de notre application Flask
app = Flask(__name__)


#FOnction "Help" affichant les requêtes possibles
@app.route('/')
def help():
    return "Guide d'utilisation : " \
            "\n\n - Créer une note : \n" \
           "      curl -H \"Content-Type:text/plain\" --data \"penser au pain\" http://localhost:8080/notes" \
           "\n      avec le contenu de la note en data" \
           "\n\n - Récupérer l'ensemble des notes : \n" \
           "      curl http://localhost:8080/notes/" \
           "\n\n - Récupérer une note à partir de son id : \n" \
           "      curl http://localhost:8080/notes/{idnote}" \
           "\n\n - Créer une note : \n" \

#Insertion d'une note dans notre base Redis
@app.route('/notes',methods=['POST'])
def notes():
    my_reddis.rpush('listeNote',request.data)
    return ('Insertion de la note faite en table \n')

#Récupération de l'ensemble des notes de notre base (DOnées retounées au format JSON
@app.route('/notes/',methods=['GET'])
def getListeNote():
    list = []
    while(my_reddis.llen('listeNote') != 0):
            list.append(my_reddis.lpop('listeNote'))
    return jsonify(str(list))

#Récupération d'une note selon son id
@app.route('/notes/<int:id>',methods=['GET'])
def getNote(id):
    return my_reddis.lindex('listeNote',id) + "\n".encode('ascii')


if __name__ == '__main__':
     app.run(host='127.0.0.1',port='8080',debug=True)
