# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
# Tạo models Bảo trì
class bt(models.Model):
    _name = "baotri.nhom1"
    _description = "Lịch sử bảo trì"

    name = fields.Char(string='Mã phiếu', required=True, default='')
    thoigianth = fields.Date('Thời gian thực hiện', required=True)
    noidung = fields.Text('Nội dung', required=True)
    chiphi = fields.Float('Chi phí', required=True)
    bt_image = fields.Binary(string='Hình ảnh biên lai')
# Tạo models Phương tiện
class phuongtien(models.Model):
    _name = "phuongtien.nhom1"
    _description = "Module vận chuyển nhóm 1"

    name = fields.Char(string='Mã Phương Tiện', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    ngaymua = fields.Date('Ngày mua')
    giamua = fields.Float('Giá mua')
    loaipt = fields.Selection([('container', 'Container'), ('xetaithung', 'Xe tải thùng')], string='Loại phương tiện', default='', required=False)
    trongtai = fields.Selection([
        ('2t', '2 tấn'),
        ('5t', '5 tấn'),
        ('7t', '7 tấn'),
        ('12-13t', '12-13 tấn'),
        ('21-22t', '21-22 tấn'),
        ('28-30t', '28-30 tấn')
    ], string='Trọng tải', default='')
    mauxe = fields.Char(string='Màu xe')
    bienso = fields.Char(string='Biển số xe', required=True, size=10)
    diachidk = fields.Char(string='Địa chỉ đăng ký')
    avatar = fields.Binary('Hình ảnh xe')
    mabh = fields.Char(string='Mã số bảo hiểm')
    ngaycap = fields.Date('Ngày cấp')
    bh_image = fields.Binary('Hình ảnh bảo hiểm')
    tinhtrang = fields.Selection([('chohoatdong', 'Chờ hoạt động'),('danghoatdong', 'Đang hoạt động'), ('dangbaotri', 'Đang bảo trì')], string='Tình trạng', default='', required=False)
    history = fields.One2many(comodel_name='baotri.nhom1', inverse_name='id', string='Lịch sử bảo trì')

    # def custom_remove(self):
    #         for module in self:
    #             module.unlink()
    #         pass

    def name_get(self):
        result = []
        for record in self:
            if len(record.bienso) == 0:
                name = record.name
            else:
                name = f"{record.bienso}"
            result.append((record.id, name))
        return result



    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('phuongtien.nhom1') or _('New')
        res = super(phuongtien, self).create(vals)
        return res




