from utils import fetch_svg, svgs_to_pdf, check_dir, page_counter

# url should look like: 
# https://vks.mtuci.ru/bigbluebutton/presentation/ab6cc0297149c9405a484f5f9ffbaa832aba4b6a-1603952740478/ab6cc0297149c9405a484f5f9ffbaa832aba4b6a-1603952740478/13330e66012653a79b1e2abb1ee9220d9be2f846-1603952786841/svg/

def main():

    check_dir()
    print('enter url')
    url = input()

    fetch_svg(url, 1)
    from utils import page_counter

    print('enter output pdf filename')
    pdf_filename = input()

    svgs_to_pdf(pdf_filename, page_counter)

    print('done!')

if __name__ == '__main__':
    main()