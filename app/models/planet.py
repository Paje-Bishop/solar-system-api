from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    mass = db.Column(db.String)

    def planet_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "mass": self.mass,
        }
