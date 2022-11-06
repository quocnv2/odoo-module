from odoo import fields, api, models, _


class HospitalAppointment(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'
    name = fields.Char(string='Name')
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    date_appointment = fields.Date(string="Date", required=True)

    def action_create_appointment(self):
        print('Clicked')
        vals = {
            'patient_id': self.patient_id.id,
            'date_appointment': self.date_appointment
        }
        self.env['hospital.appointment'].create(vals)
