from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SharedNote(models.Model):
    _name = 'sgm_bloc_notas.note'
    _description = 'Nota compartida'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Título',
        required=True,
        tracking=True
    )

    content = fields.Html(
        string='Contenido'
    )

    image = fields.Image(
        string='Imagen'
    )

    owner_id = fields.Many2one(
        comodel_name='res.users',
        string='Propietario',
        default=lambda self: self.env.user,
        required=True,
        tracking=True
    )

    category_id = fields.Many2one(
        comodel_name='sgm_bloc_notas.category',
        string='Categoría'
    )

    tag_ids = fields.Many2many(
        comodel_name='sgm_bloc_notas.tag',
        relation='sgm_bloc_notas_note_tag_rel',
        column1='note_id',
        column2='tag_id',
        string='Etiquetas'
    )

    line_ids = fields.One2many(
        comodel_name='sgm_bloc_notas.note_line',
        inverse_name='note_id',
        string='Líneas de la nota'
    )

    is_public = fields.Boolean(
        string='Pública',
        default=False
    )

    last_update = fields.Datetime(
        string='Última actualización',
        compute='_compute_last_update',
        store=True
    )

    @api.depends('write_date')
    def _compute_last_update(self):
        for record in self:
            record.last_update = record.write_date

    @api.constrains('name')
    def _check_name_not_empty(self):
        for record in self:
            if record.name and len(record.name.strip()) < 3:
                raise ValidationError(
                    'El título de la nota debe tener al menos 3 caracteres.'
                )
