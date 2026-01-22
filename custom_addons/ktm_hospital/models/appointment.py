from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'

    
    reference = fields.Char(string='Reference', default='New')
    # name = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True, default=lambda self: 'New',tracking=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True, tracking=True,ondelete='cascade')
    
    patient_gender = fields.Selection(related='patient_id.gender', string="Gender", readonly=True)
    patient_dob = fields.Date(related='patient_id.date_of_birth', string="Date of Birth", readonly=True)
    
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True, tracking=True)
    appointment_date = fields.Date(string="Date", default=fields.Date.context_today, tracking=True)
    notes = fields.Text(string="Clinical Notes", tracking=True)


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('reference', 'New') == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)