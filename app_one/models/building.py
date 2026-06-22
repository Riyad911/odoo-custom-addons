from odoo import models, fields


class Building(models.Model):
    _name = 'building'
    _description = 'Building Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    #We don't need the _rec_name because the name it is Reserved Field.
    #_rec_name = 'code'


    num = fields.Integer()
    code = fields.Char()
    description = fields.Text()
# These are Reserved Field
    name = fields.Char()
    active = fields.Boolean(default=True)





