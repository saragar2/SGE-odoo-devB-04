from odoo import models, fields


class SharedNoteLine(models.Model):
    _name = 'sgm.note_line'
    _description = 'Línea de nota'

    note_id = fields.Many2one(
        comodel_name='sgm.note',
        string='Nota',
        required=True,
        ondelete='cascade'
    )

    title = fields.Char(
        string='Título',
        required=True
    )

    description = fields.Text(
        string='Descripción'
    )

    done = fields.Boolean(
        string='Completada',
        default=False
    )
