# -*- coding: utf-8 -*-

import xlrd, xlwt, xlutils

def read_excel(filename):
    '''
    读取excel文件内容
    :param filename:  需要打开的文件名称
    :return:  无返回 只打印
    '''
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_name('Sheet1')
    rows = sheet.nrows
    # cols = sheet.ncols
    # for c in range(cols):
    #     c_values = sheet.col_values(c)
    #     print c_values
    for r in range(rows):
        r_values = sheet.row_values(r)
        print r_values

    # print (sheet.cell(1, 1))  #指定位置打印

def write_excel(filename, data):
    '''
    将data写入Excel文件
    :param filename:  文件名
    :param data: 这是一个列表，列表中的元素也是一个列表，每个元素代表一行
    :return:无返回
    '''
    book = xlwt.Workbook(encoding='utf-8')  #创建一个对象
    sheet = book.add_sheet('Sheet1')  #给这个对象添加一个sheet
    c = 0   #从第一行开始
    for d in data:   #遍历列表
        for index in range(len(d)):
            # 将子列表的每一个元素写入文件
            sheet.write(c, index, d[index])  #sheet.write（第几行， 第几列， 写入的数据）
        c += 1 #祥一行
    book.save(filename) #将这个对象一次性存到文件里，减少IO操作



def main():
    data = []
    with open('title.txt', 'r') as f:

        for line in f:
            tem_list = line.split(' ', 2)
            data.append(tem_list)

    write_excel('aaa.xlsx', data)
    read_excel('aaa.xlsx')

if __name__ == '__main__':
    main()