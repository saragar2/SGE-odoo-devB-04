from odoo import models, fields


class SharedNoteTag(models.Model):
    _name = 'sgm.tag'
    _description = 'Etiqueta de nota'

    name = fields.Char(
        string='Nombre',
        required=True
    )

    color = fields.Integer(
        string='Color'
    )

    note_ids = fields.Many2many(
        comodel_name='sgm.note',
        string='Notas'
    )
