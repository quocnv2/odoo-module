from odoo import fields, api, models, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male', "Male"), ('female', "Female"), ('other', "Other")], default='other',
                              required=True)
    reference = fields.Char(string="Order Reference", required=False, copy=False, readonly=True,
                            default=lambda self: _('New'), store=True)
    note = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft', tracking=True)

    responsible_id = fields.Many2one('res.partner', string="Responsible ID")
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointment ID')
    appointment_count = fields.Integer(string='Appointment Count', tracking=True, compute='_compute_appointment_count')
    image = fields.Binary(string="Patient Image")

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        # print("Successfully overided create method")
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        return super(HospitalPatient, self).create(vals)

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])
            rec.appointment_count = appointment_count

    @api.model
    def default_get(self, vals):
        result = super(HospitalPatient, self).default_get(vals)
        return result
