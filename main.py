import os
import shutil

from utils import fetch_svg, svgs_to_pdf
from requests.exceptions import MissingSchema

# url should look like:
# https://vks.mtuci.ru/bigbluebutton/presentation/ab6cc0297149c9405a484f5f9ffbaa832aba4b6a-1603952740478/ab6cc0297149c9405a484f5f9ffbaa832aba4b6a-1603952740478/13330e66012653a79b1e2abb1ee9220d9be2f846-1603952786841/svg/


def parse(url, pdf_filename):

    your_dir = os.path.dirname(os.path.abspath(__file__))

    directory_svg = 'svg'
    directory_pdf = 'pdf'

    for directory in [directory_svg, directory_pdf]:
        path = os.path.join(your_dir, directory)

        try:
            os.mkdir(path)
        except OSError:
            pass

    page_counter = fetch_svg(url)

    if page_counter > 0:

        svgs_to_pdf(pdf_filename, page_counter)

        for directory in [directory_svg, directory_pdf]:
            path = os.path.join(your_dir, directory)

            try:
                shutil.rmtree(path)
            except OSError as e:
                print(e.strerror)
        print(f'Parsing {pdf_filename} is done!!')

    else:
        print('что-то пошло не так, проверьте ссылку')


if __name__ == '__main__':
    print('введите url до .../svg/')
    url = input()
    print('введите название pdf файла')
    pdf_name = input()
    try:
        parse(url, pdf_name)
    except MissingSchema as error:
        print(error)
