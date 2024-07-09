import csv
import zipfile
from pypdf import PdfReader
from script_os import ZIP_DIR
from openpyxl import load_workbook
import datetime



def test_pdf():
        with zipfile.ZipFile(ZIP_DIR) as zip_file:
                with zip_file.open('KPI.pdf') as pdf_file:
                        reader = PdfReader(pdf_file)
                        number_of_pages = len(reader.pages)
                        print(number_of_pages)
                        page = reader.pages[0]
                        text = page.extract_text()
                assert 'Качественный показатель' in text



def test_xlsx():
        with zipfile.ZipFile(ZIP_DIR) as zip_f:
                with zip_f.open('characters.xlsx') as xlsx_file:
                        workbook = load_workbook(xlsx_file)
                        sheet = workbook.active
                        for x in sheet.columns:
                                assert sheet['B7'].value == 'Берест Владимир'
                                assert sheet['C7'].value == datetime.datetime(1999, 1, 5, 0, 0)
                                assert sheet['D4'].value == 'Первое появление в главе'


def test_csv():
        with zipfile.ZipFile(ZIP_DIR) as zip_f:
                with zip_f.open('characters_story.csv') as csv_file:
                        content = csv_file.read().decode('utf-8-sig')
                        csvreader = list(csv.reader(content.splitlines()))
                        second_row = csvreader[1]
                        assert second_row[0] == 'Беликов Юрий;14.06.2001;глава 1'


