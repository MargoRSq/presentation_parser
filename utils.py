import os
import io
import aiohttp
import asyncio

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PyPDF2 import PdfFileMerger, PdfFileReader


async def parse_svgs(url: str) -> list:
    async with aiohttp.ClientSession() as session:
        svg_array = []
        page_num = 1
        first_request = await session.get(url + str(page_num))
        status = first_request.status
        
        while status == 200:
            async with session.get(url + str(page_num)) as resp:
                status = resp.status
                page_num += 1
                if status == 200:
                    svg_array.append(await resp.read())
        return svg_array



def converter(url: str, pdf_filename: str, dir: str) -> None:
    mergedObject = PdfFileMerger()
    
    loop = asyncio.get_event_loop()
    svgs = loop.run_until_complete(parse_svgs(url))
    
    for svg in svgs:
        
        svg = io.BytesIO(svg)
        drawing = svg2rlg(svg)
        pdf = io.BytesIO(renderPDF.drawToString(drawing))

        mergedObject.append(PdfFileReader(pdf))       

    mergedObject.write(dir + f'\pdf\{pdf_filename}.pdf')