from odoo import fields, api, models, _


class HospitalAppointment(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'
    name = fields.Char(string='Name', required=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)

    def action_create_appointment(self):
        print('Clicked')
