from odoo import _, api, fields, models
class nhanvien(models.Model):
    _inherit = 'hr.employee'
    _description = "Prototype inheritance_kế thừa từ model nhân viên trong odoo"
