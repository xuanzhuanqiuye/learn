import xlrd
import xlwt

styleOK = xlwt.easyxf()
styleok1= xlwt.easyxf()

pattern = xlwt.Pattern()  # 一个实例化的样式类
pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # 固定的样式
pattern.pattern_fore_colour = xlwt.Style.colour_map['light_turquoise']

borders = xlwt.Borders()  # 为样式创建边框
borders.left = 2
borders.right = 2
borders.top = 6
borders.bottom = 2

font = xlwt.Font()  # 为样式创建字体
font.name = '宋体'
font.bold = False
font.height = 220

ali=xlwt.Alignment()
ali.vert=0x01
ali.horz=0x02


styleOK.pattern = pattern
styleOK.borders = borders
styleOK.font = font
styleOK.alignment=ali

styleok1.borders=borders
styleok1.font=font
styleok1.alignment=ali


wb = xlwt.Workbook()
ws = wb.add_sheet('模板',cell_overwrite_ok=True)  # 增加sheet
rows1=['设备编号','设备地址','设备类型','设备品牌','实际平均技术可用率','全省目标平均技术可用率','实际平均维护时间(小时)',
      '全省目标平均维护时间(小时)','报修时间','到达时间','完成时间','到达时长(小时)','维护时长(小时)','服务类型(维修\维护\支持)'
    ,'故障描述','解决方法'
]
rows2=['-','-','CRS','怡化','-','98.50%','-','-','-','-','-','-','-','-','-','-'
]
for index, val in enumerate(rows1):
    ws.col(index).width = 150 * 30 # 定义列宽
    ws.write(0, index, val,styleOK)
for index, val in enumerate(rows2):
    ws.col(index).width = 150 * 30 # 定义列宽
    ws.write(1, index, val,styleok1)

wb.save('data/learn.xls')