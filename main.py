import os

from utils import converter
from requests.exceptions import MissingSchema

# url should look like:
# https://vks.mtuci.ru/bigbluebutton/presentation/ab6cc0297149c9405a484f5f9ffbaa832aba4b6a-1603952740478/ab6cc0297149c9405a484f5f9ffbaa832aba4b6a-1603952740478/13330e66012653a79b1e2abb1ee9220d9be2f846-1603952786841/svg/


def main(url: str, pdf_filename: str) -> None:

    your_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_pdf_folder = os.path.join(your_dir, 'pdf')

    try:
        os.mkdir(path_to_pdf_folder)
    except OSError:
        pass
    
    try:
        converter(url, pdf_filename, your_dir)
    except MissingSchema:
        print('Проверьте правильность введенной ссылки!')


if __name__ == '__main__':
    print('Введите url до .../svg/')
    url = input()
    print('Введите название pdf файла')
    pdf_filename = input()
    
    main(url, pdf_filename)

