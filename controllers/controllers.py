# -*- coding: utf-8 -*-
# from odoo import http


# class StorageFee(http.Controller):
#     @http.route('/storage_fee/storage_fee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/storage_fee/storage_fee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('storage_fee.listing', {
#             'root': '/storage_fee/storage_fee',
#             'objects': http.request.env['storage_fee.storage_fee'].search([]),
#         })

#     @http.route('/storage_fee/storage_fee/objects/<model("storage_fee.storage_fee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('storage_fee.object', {
#             'object': obj
#         })
