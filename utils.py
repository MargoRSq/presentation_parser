import os
import requests
import shutil

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PyPDF2 import PdfFileMerger, PdfFileReader


your_dir = os.path.dirname(os.path.abspath(__file__))


def fetch_svg(url, page_num=1, page_counter=0):

    response = requests.get(url + str(1))

    while response.status_code == 200:

        response = requests.get(url + str(page_num))
        absolute = os.path.join(your_dir, f'svg\\{page_num}.svg')

        page_num += 1
        page_counter += 1

        with open(absolute, 'w+') as f:
            f.write(response.text)

    return page_counter


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
