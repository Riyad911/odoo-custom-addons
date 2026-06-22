from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'
    _description = 'Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(default='NEW', size=8)
    description = fields.Text(tracking=1)
    postcode = fields.Char()
    date_availability = fields.Date(tracking=1)
    expected_selling_date = fields.Date(tracking=1)
    is_late = fields.Boolean()
    expected_price = fields.Float()
    selling_price = fields.Float()
    different = fields.Float(compute='_compute_diff', store=1, readonly=0)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    #To allow make archive for record without delete it.
    active = fields.Boolean(default=True)

    garden_orientation = fields.Selection([
        ('north', 'North'),  # First value is stored in the database, second is shown to the user
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], default="north")


    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')

    owner_phone = fields.Char(related="owner_id.phone", readonly=0 )
    owner_address = fields.Char(related="owner_id.address", store=1)


    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('closed', 'Closed'),
    ], default="draft")

# Validation in database
    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This name is exist!')
    ]

    bedroom_line_ids = fields.One2many('property.line.bedroom', 'property_id')
    garden_line_ids = fields.One2many('property.line.garden', 'property_id')

    @api.depends('expected_price', 'selling_price', 'owner_id.phone')
    def _compute_diff(self):
        for rec in self:
            print("compute differance is work")
            rec.different = rec.expected_price - rec.selling_price

    @api.onchange('expected_price')
    def _onchange_expected_price(self):
        for rec in self:
            print(rec)
            print("onchange expected price is work")
            return {
                'warning' : {'title': 'warning', 'message': 'negative value.', 'type': 'notification'}
            }
# Validation in logic
    '''
    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError("please add valid number of bedrooms")
    '''

    def action_draft(self):
        for rec in self:
            print("function draft is work")
            rec.state = 'draft' # we should choose the value stored in database not what see the user ('Draft')

    def action_pending(self):
        for rec in self:
            print("function pending is work")
            rec.state = 'pending'

    def action_sold(self):
        for rec in self:
            print("function sold is work")
            rec.state = 'sold'

    def action_closed(self):
        for rec in self:
            print("function closed is work")
            rec.state = 'closed'

    def check_expected_selling_date(self):
        property_ids = self.search([])
        for rec in property_ids:
            if rec.expected_selling_date and rec.expected_selling_date < fields.date.today():
                rec.is_late = True


    '''
    #CRUD
    @api.model_create_multi
    def create(self, vals):
        res = super(Property, self).create(vals)
        print("inside create method")
        return res

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        res = super(Property, self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
        print("inside read (search) method")
        return res

    def write(self, vals):
        res = super(Property, self).write(vals)
        print("(update)This function doesn't need to decorator")
        return res

    def unlink(self):
        res = super(Property, self).unlink()
        print("(Delete)This function doesn't need to decorator")
        return res
    '''



class PropertyLineBedroom(models.Model):
    _name = 'property.line.bedroom'

    property_id = fields.Many2one('property')
    area = fields.Float()
    description = fields.Char()

class PropertyLineGarden(models.Model):
    _name = 'property.line.garden'

    property_id = fields.Many2one('property')
    area = fields.Float()
    description = fields.Char()