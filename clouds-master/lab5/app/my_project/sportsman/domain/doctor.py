from my_project.database import db
from sqlalchemy import ForeignKey


class Doctor(db.Model):
    __tablename__ = "doctor"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    doctor_specialization_id = db.Column(
        db.Integer,
        ForeignKey('doctor_specialization.id'),
        nullable=False
    )
    doctor_contact_id = db.Column(   # Python-side name
        "doctors_contact_id",        # DB column name
        db.Integer,
        ForeignKey('doctors_contact.id'),
        unique=True,
        nullable=False
    )

    specialization = db.relationship('DoctorSpecialization', back_populates='doctors')
    contact = db.relationship('DoctorsContact', back_populates='doctors')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "doctor_specialization_id": self.doctor_specialization_id,
            "doctor_contact_id": self.doctor_contact_id,  # singular for API
        }
