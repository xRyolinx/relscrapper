import openpyxl
from openpyxl.styles import Alignment
import os.path


def getFileName(params):
    filename = params['filename']
    
    stop = False
    i = 1
    while not stop:
        check = os.path.isfile(filename)
        if check:
            filename = f'linkedin({i}).xlsx'
        else:
            stop = True
        i += 1

    return filename


def saveToExcel(profiles, params):
    # get usable file name
    filename = getFileName(params)

    # Create a new Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Add headers to the Excel sheet
    headers = ["Nom", "Informations", "Lien LINKEDIN"]
    sheet.append(headers)

    # Add data to the Excel sheet
    for profil in profiles:
        sheet.append([profil['name'], profil['infos'], profil['link']])


    # set style
    sheet.column_dimensions["A"].width = 50.0
    sheet.column_dimensions["B"].width = 50.0
    sheet.column_dimensions["C"].width = 50.0

    for row in sheet.iter_rows():
        for cell in row:
            cell.alignment = Alignment(wrapText=True, vertical='center')

    # Save the workbook to a file
    workbook.save(filename)

    # Print a success message
    print("Excel file created successfully!")