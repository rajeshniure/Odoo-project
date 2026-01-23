from odoo import api, fields, models


class ContactMove(models.Model):
    _inherit = 'res.partner'

    social_handles = fields.Char(string='Social Handles')
    emergency_contact = fields.Char(string='Emergency Contact')