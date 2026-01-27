from datetime import date
from odoo import api, fields, models


class ContactMove(models.Model):
    _inherit = 'res.partner'

    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")], string="Gender", tracking=True
    )
    age = fields.Integer(
        string="Age", compute="_compute_age", store=True, tracking=True
    )

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