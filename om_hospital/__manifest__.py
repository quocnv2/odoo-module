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
        'views/patient.xml',
        'views/sale.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
