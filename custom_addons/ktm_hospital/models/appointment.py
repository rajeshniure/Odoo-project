from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'

    name = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True, default=lambda self: 'New',tracking=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True, tracking=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True, tracking=True)
    appointment_date = fields.Date(string="Date", default=fields.Date.context_today, tracking=True)
    notes = fields.Text(string="Clinical Notes", tracking=True)