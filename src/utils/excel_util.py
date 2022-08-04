import xlrd


def open_work(path):
    wb = xlrd.open_workbook(path)
    return wb


