from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'

    name = fields.Char(string="Order Reference", required=False, copy=False, readonly=True,
                       default=lambda self: _('New'), store=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Hospital Doctor", required=True)
    age = fields.Integer(string='Age', related='patient_id.age', tracking=True)
    gender = fields.Selection([('male', "Male"), ('female', "Female"), ('other', "Other")], default='other',
                              required=True)
    note = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft', tracking=True)
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Check Up Time")
    prescription = fields.Text(string="Prescription")

    prescription_line_ids = fields.One2many('appointment.prescription.lines', 'appointment_id',
                                            string='Prescription Line ID')

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
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        return super(HospitalAppointment, self).create(vals)

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
            if self.patient_id.note:
                self.note = self.patient_id.note
        else:
            self.gender = ''

    def unlink(self):
        if self.state == 'done':
            raise ValidationError("You can't delete this record in done state")
        return super(HospitalAppointment, self).unlink()


class AppointmentPrescriptionLines(models.Model):
    _name = 'appointment.prescription.lines'
    _description = "Appointment Prescription Lines"

    name = fields.Char(string="Medicine", required=True)
    qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment ID")
