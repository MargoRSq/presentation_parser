import os
import requests

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PyPDF2 import PdfFileMerger, PdfFileReader


your_dir = os.path.dirname(os.path.abspath(__file__))
page_counter = 0


def fetch_svg(url, page_num):
    global page_counter

    response = requests.get(url + str(page_num))

    if response.status_code == 200:
        absolute = os.path.join(your_dir, f'svg\\{page_num}.svg')

        with open(absolute, 'w+') as f:
            f.write(response.text)

        page_num += 1
        page_counter += 1
        fetch_svg(url, page_num)


def svgs_to_pdf(pdf_filename, page_num):
    mergedObject = PdfFileMerger()

    for page in range(1, page_num):
        path_to_svg = os.path.join(your_dir, 'svg/')
        path_to_pdf = os.path.join(your_dir, 'pdf/')
        
        drawing = svg2rlg(path_to_svg + f'{page}.svg')

        renderPDF.drawToFile(drawing, path_to_pdf + f'{page}.pdf')
        mergedObject.append(PdfFileReader(path_to_pdf + f'{page}.pdf', 'rb'))

    where_to = os.path.join(your_dir, f'{pdf_filename}.pdf')
    mergedObject.write(where_to)

def check_dir():
    directory_svg = 'svg'
    directory_pdf = 'pdf'

    for directory in [directory_svg, directory_pdf]:
        path = os.path.join(your_dir, directory)
        try: 
            os.mkdir(path) 
        except OSError:
            pass
