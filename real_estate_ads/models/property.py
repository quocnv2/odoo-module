from odoo import models, fields


class Property(models.Model):
    _name = 'estate.property'
    name = fields.Char(string='Name', required=True)
    type_tags = fields.Many2many('estate.property.tag', string="Type Tags")
    type_id = fields.Many2one('estate.property.type', string="Type ID")
    description = fields.Char(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string="Available From")
    expected_price = fields.Float(string="Expected Price")
    best_offer = fields.Float(string="Best Offer")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area(sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=False)
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string="Garden Orientation", default='north')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    sales_id = fields.Many2one('res.users', string="Salesman")
    buyer_id = fields.Many2one('res.partner', string="Buyer")
    total_area = fields.Integer(string="Total Area")


class PropertyType(models.Model):
    _name = 'estate.property.type'
    name = fields.Char(string='Name', required=True)


class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    name = fields.Char(string='Name', required=True)
