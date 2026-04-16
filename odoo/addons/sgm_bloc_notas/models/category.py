from odoo import models, fields


class SharedNoteCategory(models.Model):
    _name = 'sgm.category'
    _description = 'Categoría de notas'

    name = fields.Char(
        string='Nombre',
        required=True
    )

    description = fields.Text(
        string='Descripción'
    )

    note_ids = fields.One2many(
        comodel_name='sgm.note',
        inverse_name='category_id',
        string='Notas'
    )
