# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacedemy.course'
    _description = 'openacedemy courses'

    name = fields.Char(string="Title",required = True)
    description = fields.Text()

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)    
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
