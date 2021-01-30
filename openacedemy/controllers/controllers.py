# -*- coding: utf-8 -*-
#   from odoo import http


# class Openacedemy(http.Controller):
#     @http.route('/openacedemy/openacedemy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacedemy/openacedemy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacedemy.listing', {
#             'root': '/openacedemy/openacedemy',
#             'objects': http.request.env['openacedemy.openacedemy'].search([]),
#         })

#     @http.route('/openacedemy/openacedemy/objects/<model("openacedemy.openacedemy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacedemy.object', {
#             'object': obj
#         })
