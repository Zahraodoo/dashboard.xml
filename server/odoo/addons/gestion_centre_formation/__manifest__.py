# -*- coding: utf-8 -*-
{
    'name': "Gestion Centre de Formation",
    'version': '0.1',
    'author': "Haioun.F.zahra / Chouib.Rima / Idiou.Nanila",
    'category': 'Gestion Formation',
    'summary': "Tools",
    'description': "Gestion Centre de formation",
    'website': "",
    'license':'LGPL-3',

    'images': [
         'getion_centre_formation/src/image/',
    ],
    # any module necessary for this one to work correctly
    'depends': ['base'],
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'views/formation.xml',
        'views/entreprise.xml',
        # 'views/enseignants.xml',
        'views/site.xml',
        'views/apprenants.xml',
        'views/inscription.xml',
        # 'views/groupe.xml',
        'views/mode_formation.xml',
        'views/type_formation.xml',
        'views/menu.xml',
        'data/mode_formation_data.xml',
        'data/type_formation_data.xml',

    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}


