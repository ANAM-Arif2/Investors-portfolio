import requests
from lxml import html
from googletrans import Translator
import csv


def kompass_info():
    url = "https://firmeneintrag.creditreform.de/14482/2012045860/GERMAN_DEEP_TECH_INNOVATIONS_AG"

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'sw=urf8wIC-HD0JF; KEYCLOAK_LOCALE=de; CAS_PREFERRED_LANGUAGE=de_DE; iadvize-7892-vuid=%7B%22vuid%22%3A%229307bcca4aa7465ba9005e620a3c4f7ebafe286f987b4%22%2C%22deviceId%22%3A%22ac884de0-c7df-4251-b91f-d494548db351%22%7D; SERVERID_CURIEFENSE=f01; rbzid=MNZ3MPNUVOZyGrWVt/LPMomdgBJaKITElrglV5Y8H20DoGQL3jR6+UP79vsuD6GOMWQi6RTBDzYBlQqTvmm4kPJQlrNI4weJ5SDNx00AQPuMCD8OoM1kipp8vm9t6DMBLen/WzNHhGUlF8Oszeihpwz0mUtSAlpsUl7kYtlp6g--; SESSION=YjM5NDdlOGMtMWNhZC00Y2QzLWJlMTEtYTJjMGIzNWZjYzBi; wt_rla=195357560818821%2C5%2C1729676899697',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://firmeneintrag.creditreform.de/suche',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }

    return requests.request("GET", url, headers=headers, data=payload)


def get_content(web_content, xpath):
    tree = html.fromstring(web_content.content)

    # Use XPath to extract data (Example: Get all headings <h1>)
    contents = tree.xpath(xpath)
    print(contents)
    for i in contents:
        print(i.text_content())
    # Print the extracted headings
    for content in contents:
        if hasattr(content, 'text_content'):
            # print(content.text_content())
            yield content.text_content().strip()
        else:
            yield content


def get_all_rows(web_content, xpath):
    tree = html.fromstring(web_content.content)

    # Use XPath to extract all <tr> elements in the table
    rows = tree.xpath(xpath)
    # Print each row separately
    for row in rows:
        row_content = row.xpath('.//text()')  # Extract all text within the <tr>
        row_content = [text.strip() for text in row_content if text.strip()]  # Clean and remove empty text
        yield row_content


def translate_text_auto(text, dest_lang):
    translator = Translator()
    try:
        # Automatically detect the source language and translate
        translated = translator.translate(text, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}", None


def create_csv_with_headers(filename, headers, **kwargs):
    """
    Creates a CSV file with specified headers and adds scraped information based on parameters.

    Parameters:
    - filename (str): The name of the CSV file to be created (e.g., 'data.csv').
    - headers (list): A list of column headers for the CSV file.
    - kwargs: Individual column values as keyword arguments. If a column value is not provided, it defaults to None.
    """
    # Open the file in append mode
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        # Write the headers only if the file is new/empty
        if file.tell() == 0:
            writer.writeheader()

        # Initialize the row with None for each header and update with provided kwargs
        row_data = {header: kwargs.get(header, None) for header in headers}
        writer.writerow(row_data)

    print(f"Data added to '{filename}' successfully!")





