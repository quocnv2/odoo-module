{
    'name': 'OM Hospital',
    'version': '1.1',
    'summary': 'Hospital Module',
    'sequence': 10,
    'description': """
""",
    'category': 'Other',
    'website': 'https://www.odoo.com',
    'depends': ['base', 'sale', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_views.xml',
        'wizard/search_appointment_view.xml',
        'views/patient.xml',
        'views/sale.xml',
        'views/kids_view.xml',
        'views/patient_gender_views.xml',
        'views/appointment.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
