# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ddd(models.TransientModel):
    _inherit = 'res.config.settings'

    portal_allow_api_keys = fields.Char()


class AccountMoveInh(models.Model):
    _inherit = 'account.move'

    def get_gross_amount(self):
        price_total = 0
        for line in self.invoice_line_ids:
            vv = line.get_unit_price_customer_tax()
            price_total = (vv*line.quantity) + price_total

        return "{:.2f}".format(price_total - self.get_vat())

    def get_vat(self):
        vat_total = 0
        for line in self.invoice_line_ids:
            product = self.env['product.pricelist.item'].search(
                [('product_id', '=', line.product_id.id), ('pricelist_id', '=', 1)], limit=1)
            vat_total = vat_total + (((product.fixed_price * line.quantity) - ((product.fixed_price* line.quantity)*(line.discount/100))) * (line.product_id.taxes_id[0].amount/100))
        return vat_total

    def get_discount_amount(self):
        discount_total = 0
        for line in self.invoice_line_ids:
            discount_total = discount_total + (line.get_line_discount() * line.quantity)
        return "{:.2f}".format(discount_total)

    def get_taxable_amount(self):
        discount_total = 0
        for line in self.invoice_line_ids:
            product = self.env['product.pricelist.item'].search(
                [('product_id', '=', line.product_id.id), ('pricelist_id', '=', 1)], limit=1)
            discount_total = discount_total + ((product.fixed_price* line.quantity) - (product.fixed_price* line.quantity)*(line.discount/100))
        return discount_total

    def get_vat_amount(self):
        vat_total = 0
        for line in self.invoice_line_ids:
            product = self.env['product.pricelist.item'].search(
                [('product_id', '=', line.product_id.id), ('pricelist_id', '=', 1)], limit=1)
            vat_total = vat_total + (((product.fixed_price * line.quantity) - (
                        (product.fixed_price * line.quantity) * (line.discount / 100))) * (
                                                 line.product_id.taxes_id[0].amount / 100))
        return vat_total


    # def get_net_amount(self):




class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    def get_unit_price(self):
        product = self.env['product.pricelist.item'].search([('product_id', '=', self.product_id.id), ('pricelist_id', '=', 1)], limit=1)
        return product.fixed_price

    def get_unit_price_customer_tax(self):
        product = self.env['product.pricelist.item'].search([('product_id', '=', self.product_id.id), ('pricelist_id', '=', 1)], limit=1)
        return (product.fixed_price*self.quantity +((product.fixed_price*self.quantity)*(self.product_id.taxes_id[0].amount/100)))

    def get_line_discount(self):
        product = self.env['product.pricelist.item'].search(
            [('product_id', '=', self.product_id.id), ('pricelist_id', '=', 1)], limit=1)
        return (product.fixed_price * self.quantity) * (self.discount / 100)








