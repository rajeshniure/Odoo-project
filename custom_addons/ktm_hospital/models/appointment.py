from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"
    _rec_name = "patient_id"

    reference = fields.Char(string="Reference", default="New")
    patient_id = fields.Many2one(
        "res.partner",
        string="Patient",
        required=True,
        tracking=True,
        ondelete="cascade",
    )
    
    doctor_id = fields.Many2one(
        "hospital.doctor", string="Doctor", required=True, tracking=True
    )

    patient_gender = fields.Selection(
        related="patient_id.gender", string="Gender", readonly=True
    )
    patient_dob = fields.Date(
        related="patient_id.date_of_birth", string="Date of Birth", readonly=True
    )
    
    patient_blood_group = fields.Selection(
        related="patient_id.blood_group", string="Blood Group", readonly=True
    )
    patient_age = fields.Char(
        related="patient_id.age", string="Age", readonly=True
    )
    patient_marital_status = fields.Selection(
        related="patient_id.marital_status", string="Marital Status", readonly=True
    )

    
    appointment_date = fields.Date(
        string="Date", default=fields.Date.context_today, tracking=True
    )
    notes = fields.Text(string="Clinical Notes", tracking=True)

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("ongoing", "Ongoing"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
        tracking=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("reference", "New") == "New":
                vals["reference"] = self.env["ir.sequence"].next_by_code(
                    "hospital.appointment"
                )
        return super().create(vals_list)

    def action_confirm(self):
        for rec in self:
            rec.state="confirmed"
            
    def action_ongoing(self):
        for rec in self:
            rec.state="ongoing"
            
    def action_done(self):
        for rec in self:
            rec.state="done"
            
    def action_cancel(self):
        for rec in self:
            rec.state="cancelled"
            
            
    def action_print_report(self):
        return self.env.ref('ktm_hospital.action_report_hospital_appointment').report_action(self)