from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Doctor Master'

    name = fields.Char(string='Name', required=True, tracking=True)
    specialty = fields.Char(string='Specialty',tracking=True)
    doctor_license = fields.Char(string='License ID',tracking=True)