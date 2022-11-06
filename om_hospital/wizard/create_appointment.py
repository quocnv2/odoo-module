from odoo import fields, api, models, _


class HospitalAppointment(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'
    name = fields.Char(string='Name')
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    date_appointment = fields.Date(string="Date")

    def action_create_appointment(self):
        print('Clicked')
        vals = {
            'patient_id': self.patient_id.id,
            'date_appointment': self.date_appointment
        }
        # patient_id = self.env['hospital.appointment'].create(vals)
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': self.env['hospital.appointment'].create(vals).id,
            'target': 'new',
        }

    def action_view_appointment(self):
        action = self.env.ref('om_hospital.appointment_actions').read()[0]
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action
