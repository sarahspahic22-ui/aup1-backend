from flask import Flask, jsonify, request
from extensions import db, migrate
from models import Pacijent, Lijecnik, Usluga, Termin
from flask_cors import CORS
from sqlalchemy import or_

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/aup1"

db.init_app(app)
migrate.init_app(app, db)

@app.route('/pacijenti', methods=['GET'])
def pacijenti():
    pacijenti = Pacijent.query.all()

    return jsonify([p.to_dict() for p in pacijenti])

@app.route('/pacijenti/<int:id>', methods=['GET'])
def pacijent(id):
    pacijent = Pacijent.query.get_or_404(id)

    return jsonify(pacijent.to_dict())

@app.route('/pacijenti', methods=['POST'])
def dodaj_pacijenta():
    podaci = request.json

    novi_pacijent = Pacijent(
        ime=podaci["ime"],
        prezime=podaci["prezime"],
        telefon=podaci["telefon"],
        email=podaci["email"]
    )

    db.session.add(novi_pacijent)
    db.session.commit()

    return jsonify(novi_pacijent.to_dict()), 201

@app.route('/pacijenti/<int:id>', methods=['PUT'])
def uredi_pacijenta(id):
    pacijent = Pacijent.query.get_or_404(id)
    podaci = request.json

    pacijent.ime = podaci["ime"]
    pacijent.prezime = podaci["prezime"]
    pacijent.telefon = podaci["telefon"]
    pacijent.email = podaci["email"]

    db.session.commit()

    return jsonify(pacijent.to_dict())

@app.route('/pacijenti/<int:id>', methods=['DELETE'])
def obrisi_pacijenta(id):
    pacijent = Pacijent.query.get_or_404(id)

    db.session.delete(pacijent)
    db.session.commit()

    return jsonify({"poruka": "Pacijent je obrisan"})

@app.route('/lijecnici', methods=['GET'])
def lijecnici():
    lijecnici = Lijecnik.query.all()

    return jsonify([l.to_dict() for l in lijecnici])

@app.route('/lijecnici/<int:id>', methods=['GET'])
def lijecnik(id):
    lijecnik = Lijecnik.query.get_or_404(id)

    return jsonify(lijecnik.to_dict())

@app.route('/lijecnici', methods=['POST'])
def dodaj_lijecnika():
    podaci = request.json

    novi_lijecnik = Lijecnik(
        ime=podaci["ime"],
        prezime=podaci["prezime"],
        specijalizacija=podaci["specijalizacija"]
    )

    db.session.add(novi_lijecnik)
    db.session.commit()

    return jsonify(novi_lijecnik.to_dict()), 201


@app.route('/lijecnici/<int:id>', methods=['PUT'])
def uredi_lijecnika(id):
    lijecnik = Lijecnik.query.get_or_404(id)
    podaci = request.json

    lijecnik.ime = podaci["ime"]
    lijecnik.prezime = podaci["prezime"]
    lijecnik.specijalizacija = podaci["specijalizacija"]

    db.session.commit()

    return jsonify(lijecnik.to_dict())


@app.route('/lijecnici/<int:id>', methods=['DELETE'])
def obrisi_lijecnika(id):
    lijecnik = Lijecnik.query.get_or_404(id)

    db.session.delete(lijecnik)
    db.session.commit()

    return jsonify({"poruka": "Lijecnik je obrisan"})


@app.route('/usluge', methods=['GET'])
def usluge():
    usluge = Usluga.query.all()

    return jsonify([u.to_dict() for u in usluge])


@app.route('/usluge', methods=['POST'])
def dodaj_uslugu():
    podaci = request.json

    nova_usluga = Usluga(
        naziv=podaci["naziv"],
        cijena=podaci["cijena"],
        trajanje=podaci["trajanje"]
    )

    db.session.add(nova_usluga)
    db.session.commit()

    return jsonify(nova_usluga.to_dict()), 201


@app.route('/usluge/<int:id>', methods=['GET'])
def usluga(id):
    usluga = Usluga.query.get_or_404(id)

    return jsonify(usluga.to_dict())


@app.route('/usluge/<int:id>', methods=['PUT'])
def uredi_uslugu(id):
    usluga = Usluga.query.get_or_404(id)
    podaci = request.json

    usluga.naziv = podaci["naziv"]
    usluga.cijena = podaci["cijena"]
    usluga.trajanje = podaci["trajanje"]

    db.session.commit()

    return jsonify(usluga.to_dict())

@app.route('/usluge/<int:id>', methods=['DELETE'])
def obrisi_uslugu(id):
    usluga = Usluga.query.get_or_404(id)

    db.session.delete(usluga)
    db.session.commit()

    return jsonify({"poruka": "Usluga je obrisana"})

@app.route('/termini', methods=['GET'])
def termini():
    termini = Termin.query.all()

    return jsonify([t.to_dict() for t in termini])


@app.route('/termini', methods=['POST'])
def dodaj_termin():
    podaci = request.json

    novi_termin = Termin(
        datum=podaci["datum"],
        vrijeme=podaci["vrijeme"],
        pacijent_id=podaci["pacijent_id"],
        lijecnik_id=podaci["lijecnik_id"],
        usluga_id=podaci["usluga_id"]
    )

    db.session.add(novi_termin)
    db.session.commit()

    return jsonify(novi_termin.to_dict()), 201

@app.route('/termini/<int:id>', methods=['GET'])
def termin(id):
    termin = Termin.query.get_or_404(id)

    return jsonify(termin.to_dict())


@app.route('/termini/<int:id>', methods=['PUT'])
def uredi_termin(id):
    termin = Termin.query.get_or_404(id)
    podaci = request.json

    termin.datum = podaci["datum"]
    termin.vrijeme = podaci["vrijeme"]
    termin.pacijent_id = podaci["pacijent_id"]
    termin.lijecnik_id = podaci["lijecnik_id"]
    termin.usluga_id = podaci["usluga_id"]

    db.session.commit()

    return jsonify(termin.to_dict())

@app.route('/termini/<int:id>', methods=['DELETE'])
def obrisi_termin(id):
    termin = Termin.query.get_or_404(id)

    db.session.delete(termin)
    db.session.commit()

    return jsonify({"poruka": "Termin je obrisan"})


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return jsonify({
        "broj_pacijenata": Pacijent.query.count(),
        "broj_lijecnika": Lijecnik.query.count(),
        "broj_usluga": Usluga.query.count(),
        "broj_termina": Termin.query.count()
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)