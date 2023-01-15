from flask import Flask, render_template, request, redirect, url_for
import mysql.connector


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def Login():
    err =" "

    if request.method == 'POST':
        
        kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
        
        username = request.form['username']
        passw = request.form['password']

        krusor = kazaliste.cursor()         
        krusor.execute("select ime,lozinka from login where ime ='"+username+"' and lozinka='" +passw+ "';")
       
        if krusor.fetchone() == None:
            err = "Došlo je do pogreške!"
           
        else:
            print("uspjesno prijavita osoba!")
            return render_template("home.html")
            
    return render_template("prijava.html", err = err)


@app.route("/sponzor",  methods=['GET', 'POST'])
def sponzor():

    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.execute("select id, naziv, ulaganje from sponzor")
    data = krusor.fetchall()

    return render_template("sponzor.html",data=data,lendata= len(data))


@app.route("/sponzor/dodajspn", methods=["POST"])
def dodaj_spn():
 
    id=request.form['idspn']
    naziv=request.form['nazivspn']
    ulaganje=request.form['ulaganjespn']


    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.execute("insert into sponzor(id,naziv,ulaganje) values (%s,%s,%s)", 
                    [id, naziv,ulaganje])
    kazaliste.commit()
    kazaliste.close()
    
    return redirect(url_for('sponzor'))


@app.route("/glumac",  methods=['GET', 'POST'])
def glumac():

    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.execute("select * from glumac")
    data = krusor.fetchall()

    return render_template("glumac.html",data=data,lendata= len(data))



@app.route("/glumac/dodajgl", methods=['POST'])
def dodaj_gl():
 
    id=request.form['idgl']
    ime=request.form['imegl']
    prezime=request.form['prezimegl']


    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.execute("insert into glumac(id,ime,prezime) values (%s,%s,%s)", 
                    [id,ime,prezime])
    kazaliste.commit()
    kazaliste.close()
    
    return redirect(url_for('glumac'))



@app.route("/zaposlenik", methods=['GET','POST'])
def zaposlenik():
 
    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.execute("select * from zaposlenik")
    data = krusor.fetchall()

    return render_template("zaposlenik.html",data=data,lendata= len(data))


@app.route("/zaposlenik/dodaj", methods=["POST"])
def dodaj_zaposlenik():
 
    id=request.form['id']
    ime=request.form['ime']
    prezime=request.form['prezime']
    oib=request.form['oib']
    dob=request.form['dob']
    broj_telefona=request.form['telbr']
    email=request.form['email']
    datum_zaposlenja=request.form['datzap']
    placa=request.form['placa']

    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.execute("insert into zaposlenik(id,ime,prezime,oib,dob,broj_telefona,email,datum_zaposlenja,placa) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                    [id, ime,prezime,oib,dob, broj_telefona,email,datum_zaposlenja,placa])
    kazaliste.commit()
    kazaliste.close()
    
    return redirect(url_for('zaposlenik'))

 
@app.route("/zaposlenik/povecaj")
def povecaj():

    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.callproc("povecaj_place",[10])
    kazaliste.commit()
    kazaliste.close()
    return redirect(url_for('zaposlenik'))


@app.route("/posjetitelj", methods=['GET','POST'])
def posjetitelj():
    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.execute("select * from posjetitelj")
    data = krusor.fetchall()

    return render_template("posjetitelj.html",data=data,lendata= len(data))


@app.route("/posjetitelj/dodajpos", methods=['POST'])
def dodaj_posjetitelj():
 
    id=request.form['idpos']
    ime=request.form['imepos']
    prezime=request.form['prezimepos']
    oib=request.form['oibpos']
    dob=request.form['dobpos']

    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.execute("insert into posjetitelj(id,ime,prezime,OIB,dob) values (%s,%s,%s,%s,%s)", 
                    [id,ime,prezime,oib,dob])
    kazaliste.commit()
    kazaliste.close()

    return redirect(url_for('posjetitelj'))


@app.route("/racun", methods=['GET','POST'])
def racun():
    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.execute("select * from racun")
    data = krusor.fetchall()

    return render_template("racun.html",data=data,lendata= len(data))


@app.route("/procedura")
def procedura():

    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.callproc("povecaj_place",[10])
    kazaliste.commit()
    kazaliste.close()
    return render_template("procedura.html")


@app.route("/procedura/unos")
def procedura_unos():

    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.callproc("nova_osoba",[1343,'Leon','Smolica','12365678901',19,1914339467,'leon.smolica@gmail.com',STR_TO_DATE('04-12-2019','%d-%m-%Y'),2900])
    kazaliste.commit()
    kazaliste.close()
    return redirect(url_for('procedura'))


@app.route("/procedura/unos2")
def procedura_unos2():

    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.callproc("nova_osoba_i_racun",[1345,'Lovro','Smolica','12365678901',19,2914339467,'lovro.smolica@gmail.com',STR_TO_DATE('04.12.2019.','%d.%m.%Y.'),2900,760,1345,1500,1600,'54331',STR_TO_DATE('16.10.2020.', '%d.%m.%Y.')])
    kazaliste.commit()
    kazaliste.close()
    return redirect(url_for('procedura'))


@app.route("/statistika")
def statistika():
    kazaliste = mysql.connector.connect(host = 'localhost', database = 'kazaliste', user = 'root', password = 'root')
    krusor = kazaliste.cursor()  
    krusor.execute("select * from posjetitelj")
    data = krusor.fetchall()

    return render_template("statistika.html",data=data,lendata= len(data))


@app.route("/pocetak")
def pocetak():
    return render_template("Navbar.html")


@app.route("/vrati")
def vrati():
    return redirect(url_for('Login')), render_template("prijava.html")


if __name__ == '__main__':
    app.run(debug=True)
