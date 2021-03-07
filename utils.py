import os
import requests
import io

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PyPDF2 import PdfFileMerger, PdfFileReader


def converter(url: str, pdf_filename: str, dir: str) -> None:
    mergedObject = PdfFileMerger()

    response = requests.get(url + str(1))
    if response.status_code == 200:
        page_num = 0

        while response.status_code == 200:

            page_num += 1
            response = requests.get(url + str(page_num))
            
            if response.status_code == 200:
                svg = io.BytesIO(response.content)
                drawing = svg2rlg(svg)
                
                pdf = io.BytesIO(renderPDF.drawToString(drawing))

                mergedObject.append(PdfFileReader(pdf))

    mergedObject.write(dir + f'\pdf\{pdf_filename}.pdf')
        
