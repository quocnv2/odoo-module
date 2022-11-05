from odoo import fields, api, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', "Male"), ('female', "Female"), ('other', "Other")], default='other',
                              required=True)
    note = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('new', 'Valid'),
        ('sent', 'Sent'),
        ('used', 'Used'),
        ('expired', 'Expired'),
        ('cancel', 'Cancelled')
    ], required=True, default='new')
