from odoo import fields, api, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male', "Male"), ('female', "Female"), ('other', "Other")], default='other',
                              required=True)
    note = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft', tracking=True)

    responsible_id = fields.Many2one('res.partner', string="Responsible ID")

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'
