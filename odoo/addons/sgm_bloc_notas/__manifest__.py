# -*- coding: utf-8 -*-
{
    'name': "sgm_bloc_notas",

    'summary': "Take your own notes and share them",

    'description': """
Una página en la que podrás escribir notas de manera sencilla y elegir si compartirlas y con quién.
    """,

    'author': "Sara García Miguel",
    'website': "https://github.com/saragar2",
    'license': 'LGPL-3',

    # Las categorías se pueden usar para filtrar módulos en el listado.
    # Consulta https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # para ver la lista completa.
    'category': 'Uncategorized',
    'version': '0.1',

    # Módulos necesarios para que este funcione correctamente.
    'depends': ['base', 'mail'],

    # Se carga siempre.
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
    # Se carga solo en modo demostración.
    'demo': [
        'demo/demo.xml',
    ],
}

