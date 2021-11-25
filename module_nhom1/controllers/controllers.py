# -*- coding: utf-8 -*-
# from odoo import http


# class Nhinem(http.Controller):
#     @http.route('/nhinem/nhinem/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nhinem/nhinem/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nhinem.listing', {
#             'root': '/nhinem/nhinem',
#             'objects': http.request.env['nhinem.nhinem'].search([]),
#         })

#     @http.route('/nhinem/nhinem/objects/<model("nhinem.nhinem"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nhinem.object', {
#             'object': obj
#         })
