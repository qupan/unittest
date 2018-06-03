#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'vaca'
__description__:'生成excel报告模板'
__mtime__:2017/6/10

'''
import xlsxwriter
import time
from readConfig import ReadConfig
from log import Log

ReadConfig = ReadConfig()
log = Log()
hpassnum = 0  # 定义一个变量，用来计算测试通过的用例数量


class Report:
    def __init__(self):
        '''从config.ini提取数据'''
        report_address = ReadConfig.get_config("DATABASE", "report_address")
        self.project_name = ReadConfig.get_config('TABLEDATA', 'project_name')
        self.version = ReadConfig.get_config('TABLEDATA', 'version')
        self.scripting_language = ReadConfig.get_config('TABLEDATA', 'Scripting_language')
        self.internet = ReadConfig.get_config('TABLEDATA', 'internet')

        self.now = time.strftime("%Y-%m-%d-%H-%M-%S ", time.localtime(time.time()))
        self.repor_tddress = report_address + self.now + 'report.xlsx'
        self.workbook = xlsxwriter.Workbook(self.repor_tddress)  # 生成的报告的路径
        self.worksheet = self.workbook.add_worksheet("测试总况")
        self.worksheet2 = self.workbook.add_worksheet("测试详情")

    def get_workaddress(self):
        '''获取生成的excel地址'''
        return self.repor_tddress

    def get_sheet(self):
        '''获取sheet表'''
        return self.worksheet

    def get_sheet2(self):
        '''获取sheet2表'''
        return self.worksheet2

    def get_format(self, font_size=14, bg_color='#C7EDCC', font_color='#000000', num=1):
        '''
        设置单元格样式
        font_size: 字体大小（默认12号）
        bg_color: 背景色值（默认豆绿色）
        font_color: 字体色值（黑色）
        num: 是否有边框（1表示有）
        '''
        cell_style =  self.workbook.add_format(
            {'align': 'center', 'valign': 'vcenter', 'border': num, 'font_size': font_size, 'bg_color': bg_color,
             'font_color': font_color})
        return cell_style

    def write_cell(self, worksheet, cl, data):
        '''
        单元格写入数据
        worksheet: 工作表
        cl: 单元格
        data: 数据
        wd: excel表
        '''
        return worksheet.write(cl, data, self.get_format())

    def write_area(self, worksheet, cl, data, sign):
        '''合并多个单元格写入数据 '''
        return worksheet.merge_range(cl, str(round(data, 2)) + sign, self.get_format())

    def write_basic(self, testcassid, testcassname, method, hope, url, data, worksheet, temp):
        '''
        把基本数据写入excel
        testcassid: 用例ID
        testcassname: 用例名称
        method: 用例方法
        hope: 预期code
        url: 接口地址
        data: 请求数据
        worksheet: 写入的工作表
        temp: 写入的行数
        '''
        item = {"t_id": testcassid, "t_name": testcassname, "t_method": method, "t_url": url,
                "t_param": '%s' % data, "t_hope": 'code: %s' % hope}
        self.write_cell(worksheet, "A" + str(temp), item["t_id"])
        self.write_cell(worksheet, "B%s" % temp, item["t_name"])
        self.write_cell(worksheet, "C%s" % temp, item["t_method"])
        self.write_cell(worksheet, "D%s" % temp, item["t_url"])
        self.write_cell(worksheet, "E%s" % temp, item["t_param"])
        self.write_cell(worksheet, "F%s" % temp, item["t_hope"])

    def write_special(self, actual, hope, worksheet, temp):
        '''
        把结果写入excel
        actual: 接口返回结果
        '''
        if actual == {}:
            self.write_cell(worksheet, "G%s" % temp, "参数缺失")
            self.write_cell(worksheet, "H%s" % temp, "失败")
        elif actual["resCode"] == hope:
            self.write_cell(worksheet, "G%s" % temp, "resCode：%s，msg：%s" % (actual["resCode"], actual["resDesc"]))
            self.write_cell(worksheet, "H%s" % temp, "通过")
        elif actual["resCode"] != hope:
            self.write_cell(worksheet, "G%s" % temp, "resCode：%s，msg：%s" % (actual["resCode"], actual["resDesc"]))
            self.write_cell(worksheet, "H%s" % temp, "失败")

    def init(self):
        '''创建项目总况表结构'''

        # 设置列宽
        self.worksheet.set_column("A:A", 15)
        self.worksheet.set_column("B:B", 20)
        self.worksheet.set_column("C:C", 20)
        self.worksheet.set_column("D:D", 20)
        self.worksheet.set_column("E:E", 20)
        self.worksheet.set_column("F:F", 20)

        # 设置行高
        for hrow in range(6):
            self.worksheet.set_row(hrow, 30)

        # 生成工作表内容
        self.worksheet.merge_range('A1:G1', '测试报告总概况', self.get_format())
        self.worksheet.merge_range('A2:G2', '测试概括', self.get_format(14, "blue", "#ffffff"))
        self.worksheet.merge_range('A3:A6', '接口自动化', self.get_format())
        self.write_cell(self.worksheet, "B3", '项目名称')
        self.write_cell(self.worksheet, "B4", '接口版本')
        self.write_cell(self.worksheet, "B5", '脚本语言')
        self.write_cell(self.worksheet, "B6", '测试网络')
        self.write_cell(self.worksheet, "C3", self.project_name)
        self.write_cell(self.worksheet, "C4", self.version)
        self.write_cell(self.worksheet, "C5", self.scripting_language)
        self.write_cell(self.worksheet, "C6", self.internet)
        self.write_cell(self.worksheet, "D3", "接口总数")
        self.write_cell(self.worksheet, "D4", "通过总数")
        self.write_cell(self.worksheet, "D5", "失败总数")
        self.write_cell(self.worksheet, "D6", "报告时间")
        self.write_cell(self.worksheet, "E6", self.now)
        self.write_cell(self.worksheet, "F3", "耗时")
        self.write_cell(self.worksheet, "G3", "得分")
        log.info('测试总况表创建成功')
        self.pie()

    def pie(self):
        '''生成饼状图'''
        chart1 = self.workbook.add_chart({'type': 'pie'})
        chart1.add_series({'name': '接口测试统计', 'categories': '=测试总况!$D$4:$D$5', 'values': '=测试总况!$E$4:$E$5', })
        chart1.set_title({'name': '接口测试统计'})
        chart1.set_style(2)     # 饼状图样式
        self.worksheet.insert_chart('A9', chart1, {'x_offset': 180, 'y_offset': 10})
        log.info('饼状图生成成功')

    def test_detail(self):
        '''创建测试详情表'''
        # 设置列宽
        self.worksheet2.set_column("A:A", 20)
        self.worksheet2.set_column("B:B", 20)
        self.worksheet2.set_column("C:C", 20)
        self.worksheet2.set_column("D:D", 20)
        self.worksheet2.set_column("E:E", 20)
        self.worksheet2.set_column("F:F", 20)
        self.worksheet2.set_column("G:G", 20)
        self.worksheet2.set_column("H:H", 20)

        # 生成工作表内容
        self.worksheet2.merge_range('A1:H1', '测试详情', self.get_format(14, "blue", "#ffffff"))
        self.write_cell(self.worksheet2, "A2", '用例ID')
        self.write_cell(self.worksheet2, "B2", '接口名称')
        self.write_cell(self.worksheet2, "C2", '接口方法')
        self.write_cell(self.worksheet2, "D2", 'URL')
        self.write_cell(self.worksheet2, "E2", '参数')
        self.write_cell(self.worksheet2, "F2", '预期结果')
        self.write_cell(self.worksheet2, "G2", '实际结果')
        self.write_cell(self.worksheet2, "H2", '测试结果')
        log.info('测试详情表创建成功')

    def close_workbook(self):
        self.workbook.close()
        log.debug('工作表关闭成功')


def main():
    a = Report()
    a.test_detail()
    a.init()
    x = a.get_sheet()
    a.write_area(x, 'F4:F6', 2,'*')
    a.close_workbook()
if __name__ == '__main__':
    main()