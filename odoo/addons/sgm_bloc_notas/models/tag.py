from odoo import models, fields


class SharedNoteTag(models.Model):
    _name = 'sgm_bloc_notas.tag'
    _description = 'Etiqueta de nota'

    name = fields.Char(
        string='Nombre',
        required=True
    )

    color = fields.Integer(
        string='Color'
    )

    note_ids = fields.Many2many(
        comodel_name='sgm_bloc_notas.note',
        relation='sgm_bloc_notas_note_tag_rel',
        column1='tag_id',
        column2='note_id',
        string='Notas'
    )
