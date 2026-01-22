from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Patient Master"

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")], string="Gender", tracking=True
    )
    image = fields.Image(string="Patient Image")
    age = fields.Integer(
        string="Age", compute="_compute_age", store=True, tracking=True
    )

    phone = fields.Char(string="Phone", tracking=True)
    email = fields.Char(string="Email")
    address = fields.Text(string="Address")

    blood_group = fields.Selection(
        [
            ("A+", "A+"),
            ("A-", "A-"),
            ("B+", "B+"),
            ("B-", "B-"),
            ("AB+", "AB+"),
            ("AB-", "AB-"),
            ("O+", "O+"),
            ("O-", "O-"),
        ],
        string="Blood Group",
        tracking=True,
    )
    marital_status = fields.Selection(
        [("single", "Single"), ("married", "Married")],
        string="Marital Status",
    )

    # appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string="Appointments")

    @api.depends("date_of_birth")
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = (
                    today.year
                    - rec.date_of_birth.year
                    - (
                        (today.month, today.day)
                        < (rec.date_of_birth.month, rec.date_of_birth.day)
                    )
                )
            else:
                rec.age = 0
