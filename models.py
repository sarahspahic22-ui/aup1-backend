from extensions import db
class Pacijent(db.Model):
    __tablename__ = "pacijenti"

    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(30), nullable=False)
    prezime = db.Column(db.String(30), nullable=False)
    telefon = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "ime": self.ime,
            "prezime": self.prezime,
            "telefon": self.telefon,
            "email": self.email
        }
class Lijecnik(db.Model):
    __tablename__ = "lijecnici"

    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(30), nullable=False)
    prezime = db.Column(db.String(30), nullable=False)
    specijalizacija = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "ime": self.ime,
            "prezime": self.prezime,
            "specijalizacija": self.specijalizacija
        }
class Usluga(db.Model):
    __tablename__ = "usluge"

    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String(100), nullable=False)
    cijena = db.Column(db.Float, nullable=False)
    trajanje = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "naziv": self.naziv,
            "cijena": self.cijena,
            "trajanje": self.trajanje
        }
class Termin(db.Model):
    __tablename__ = "termini"

    id = db.Column(db.Integer, primary_key=True)
    datum = db.Column(db.String(20), nullable=False)
    vrijeme = db.Column(db.String(10), nullable=False)

    pacijent_id = db.Column(db.Integer, db.ForeignKey("pacijenti.id"), nullable=False)
    lijecnik_id = db.Column(db.Integer, db.ForeignKey("lijecnici.id"), nullable=False)
    usluga_id = db.Column(db.Integer, db.ForeignKey("usluge.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "datum": self.datum,
            "vrijeme": self.vrijeme,
            "pacijent_id": self.pacijent_id,
            "lijecnik_id": self.lijecnik_id,
            "usluga_id": self.usluga_id
        }