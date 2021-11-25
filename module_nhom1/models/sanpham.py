from odoo import _, api, fields, models
class sanpham(models.Model):
    _inherit = 'product.template'
    _description = "Sản phẩm kế thừa của sản phẩm"
