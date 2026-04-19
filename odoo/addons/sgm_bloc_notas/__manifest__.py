# -*- coding: utf-8 -*-
{
    'name': "sgm_bloc_notas",

    'summary': "Take your own notes and share them",

    'description': """
Una página en la que podrás escribir notas de manera sencilla y elegir si compartirlas y con quién.
    """,

    'author': "Sara García Miguel",
    'website': "https://github.com/saragar2",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
    	'views/menu.xml',
        'views/views.xml',
        'views/templates.xml',
		'views/note_views.xml',
		'views/note_line_views.xml',
		'views/category_views.xml',
		'views/tag_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

