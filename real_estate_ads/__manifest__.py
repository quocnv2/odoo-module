{
    'name': 'Real Estate Ad',
    'version': '0.1',
    'summary': 'New Module',
    'sequence': 10,
    'description': """""",
    'category': 'Other',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_views.xml',
        'views/property_type_views.xml',
        'views/property_tag_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
