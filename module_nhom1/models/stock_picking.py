from odoo import api, fields, models
from datetime import datetime
class stock(models.Model):
    _inherit = "stock.picking"
    _description = "Module giao hàng nhóm 1 kế thừa từ odoo"

    tinhtrang_phieu = fields.Selection([
        ('wait', 'Chờ chuyển'),
        ('doing', 'Đang chuyển'),
        ('done', 'Đã chuyển'),
        ('delay', 'Trì hoãn chuyển')
    ], string='Tình trạng phiếu', default='wait',)
    # sử dụng vòng lập foreach để lấy danh sách vào trong Selection (làm sau)
    ngaytao_phieu = fields.Date(string='Ngày tạo phiếu ', default=datetime.today(), readonly="1")
    # --- Đợi bình yên để kế thừa
    # id_xe_phieu = fields.Char('Xe giao hàng')

    id_xe_phieu = fields.Many2one('phuongtien.nhom1', string="Xe giao hàng", delegate=True, default=1)
    id_shipper_phieu = fields.Many2one('shipper.nhom1', string="Người giao hàng", delegate=True, default=1)
    id_nhanvien_taophieu = fields.Many2one('hr.employee', string="Nhân viên tạo phiếu", delegate=True, default=4)

    # 1. Kế thừa ID xe_phieu -> phuongtien_nhom1
    # 2. Cập nhật trạng thái chờ đơn hàng khi phiếu chuyển sang done
    # 3. Lọc seleced 3 khóa tham chiếu
    # 4. xét điều kiện edit trạng thái phiếu phải là tài khoản khác k được 2 tài khoản mặc định -> xuất thông báo


    @api.constrains('tinhtrang_phieu', 'id_xe_phieu')
    def onchange_status_traffic(self):
        print(self.id_xe_phieu)
        get_id_traffic = str(self.id_xe_phieu)[17:].strip('(,)')
        if self.tinhtrang_phieu in ['doing','delay']:
            self.env.cr.execute("""UPDATE phuongtien_nhom1 SET tinhtrang='danghoatdong' WHERE id = """ + get_id_traffic)
        else:
            self.env.cr.execute("""UPDATE phuongtien_nhom1 SET tinhtrang='chohoatdong' WHERE id = """ + get_id_traffic)


    @api.constrains('tinhtrang_phieu','id_shipper_phieu')
    def onchange_status_shipper(self):
        print(self.id_shipper_phieu)
        get_id_shipper = str(self.id_shipper_phieu)[13:].strip('(,)')
        if self.tinhtrang_phieu in ['doing','delay']:
            self.env.cr.execute("""UPDATE shipper_nhom1 SET trangthai='danggiaohang' WHERE id = """+get_id_shipper)
        else:
            self.env.cr.execute("""UPDATE shipper_nhom1 SET trangthai='chogiaohang' WHERE id = """ + get_id_shipper)

    @api.model
    def create_shipper_employee_main(self):
        # Khởi tạo shipper để tránh null dữ liệu khi confirm ở model SALES
        query_init_shipper = """INSERT INTO shipper_nhom1 (id, name, ten, idbanglai) 
                                SELECT * FROM (SELECT 1 AS id, '' AS name, '' AS ten, '' AS idbanglai) AS tmp 
                                WHERE NOT exists ( SELECT id FROM shipper_nhom1 WHERE id = 1 limit 1 )"""
        self.env.cr.execute(query_init_shipper)
    @api.model
    def create_employee_employee_main(self):
        # Khởi tạo shipper để tránh null dữ liệu khi confirm ở model SALES
        query_init_employee = """INSERT INTO hr_employee (id, name, company_id, resource_id) 
                                 SELECT * FROM (SELECT 4 AS id, '' AS name, 1 as company_id, 1 as resource_id) AS tmp 
    			                 WHERE NOT exists ( SELECT id FROM hr_employee WHERE id = 4 limit 1 );"""
        self.env.cr.execute(query_init_employee)
    @api.model
    def create_traffic_traffic_main(self):
        query_init_traffic = """INSERT INTO phuongtien_nhom1 (id, name, loaipt, bienso, tinhtrang ) 
                                SELECT * FROM (SELECT 1 AS id, '' AS name, '' AS loaipt, '' as bienso, '' as tinhtrang) AS tmp 
            			        WHERE NOT exists ( SELECT id FROM phuongtien_nhom1 WHERE id = 0 limit 1 );"""
        self.env.cr.execute(query_init_traffic)


    # @api.constrains('tinhtrang_phieu','id_shipper_phieu')
    # def onchange_status_shipper(self):
    #     if self.tinhtrang_phieu == 'doing':
    #         get_id_shipper = str(self.id_shipper_phieu).strip('shipper.nhom1(,)')
    #         self.env.cr.execute("""Update shipper_nhom1 set trangthai='danggiaohang' where id = """+get_id_shipper)


    # id_khachhang = fields.One2many(comodel_name='res.users', inverse_name='rel_id')