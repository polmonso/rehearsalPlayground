import gspread

gc = gspread.login('tunabrix@gmail.com', '')

spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1pMbPMieX_QMBrjVL4-yPmbOElMoIFDOQb3eXYRnHOgM/edit?pli=1#gid=0')

worksheet = spreadsheet.sheet1

cell_list = worksheet.range('D21:D23')

for cell in cell_list:
    if cell.value == '':
        cell.value = 'TunaBrix!'

worksheet.update_cells(cell_list)

