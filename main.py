import os
import requests

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PyPDF2 import PdfFileMerger, PdfFileReader


# url should look like: 
# https://vks.mtuci.ru/bigbluebutton/presentation/ab6cc0297149c9405a484f5f9ffbaa832aba4b6a-1603952740478/ab6cc0297149c9405a484f5f9ffbaa832aba4b6a-1603952740478/13330e66012653a79b1e2abb1ee9220d9be2f846-1603952786841/svg/

print('enter url')
url = input()

your_dir = os.path.dirname(os.path.abspath(__file__))

print('waiting...')

page_num = 1

while True:

    response = requests.get(url + str(page_num))

    if response.status_code == 200:
        absolute = os.path.join(your_dir, f'svg\\{page_num}.svg')

        with open(absolute, 'w+') as f:
            f.write(response.text)
            page_num += 1

    else:
        break

mergedObject = PdfFileMerger()

for page in range(1, page_num):
    path_to_svg = os.path.join(your_dir, 'svg/')
    path_to_pdf = os.path.join(your_dir, 'pdf/')
    
    drawing = svg2rlg(path_to_svg + f'{page}.svg')

    renderPDF.drawToFile(drawing, path_to_pdf + f'{page}.pdf')
    mergedObject.append(PdfFileReader(path_to_pdf + f'{page}.pdf', 'rb'))

print('enter output pdf filename')
output_pdf = input()

where_to = os.path.join(your_dir, f'{output_pdf}.pdf')
mergedObject.write(where_to)

print('done!')
