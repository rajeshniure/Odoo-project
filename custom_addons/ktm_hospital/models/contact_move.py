from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
from odoo import api, fields, models


class ContactMove(models.Model):
    _inherit = 'res.partner'

    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")], string="Gender", tracking=True
    )
    age = fields.Char(
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
    
    
    # @api.depends("date_of_birth")
    # def _compute_age(self):
    #     for rec in self:
    #         if rec.date_of_birth:
    #             if rec.date_of_birth > date.today():
    #                 raise ValidationError("The Date of Birth cannot be in the future!")
    #                 # continue
                    
    #             d1 = rec.date_of_birth
    #             d2 = date.today()
    #             diff = relativedelta(d2, d1)
    #             rec.age = f"{diff.years} Years, {diff.months} Months, {diff.days} Days"
    #         else:
    #             rec.age = "N/A"
    
    @api.onchange('date_of_birth')
    def _onchange_date_of_birth(self):
        if self.date_of_birth and self.date_of_birth > date.today():
            raise ValidationError("The Date of Birth cannot be in the future!")
        
    # @api.constrains('date_of_birth')
    # def _check_date_of_birth(self):
    #     for rec in self:
    #         if rec.date_of_birth and rec.date_of_birth > date.today():
    #             raise ValidationError("The Date of Birth cannot be in the future!")

    @api.depends("date_of_birth")
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth <= date.today():
                diff = relativedelta(date.today(), rec.date_of_birth)
                rec.age = f"{diff.years}Years {diff.months}Months {diff.days}Days"
            else:
                rec.age = "N/A"