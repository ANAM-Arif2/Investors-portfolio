import requests
# from lxml import html
from googletrans import Translator
import csv
import re
from bs4 import BeautifulSoup

def creditform_info():
    url = "https://firmeneintrag.creditreform.de/14482/2013252364/GERMAN_DEEP_TECH_QUANTUM_2140_VERMOEGENSVERWALTUNGSGESELLSCHAFT_MBH"

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


# def get_content(web_content, xpath):
#     tree = html.fromstring(web_content.content)
#
#     # Use XPath to extract data
#     contents = tree.xpath(xpath)
#
#     # Extract text content if available and return as a list
#     result = []
#     for content in contents:
#         if hasattr(content, 'text_content'):
#             result.append(content.text_content().strip())
#         else:
#             result.append(content)
#
#     return result


def get_content_bs4(web_content, css_selector, index=0):
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(web_content.content, 'html.parser')

    # Use CSS selector to extract data
    elements = soup.select(css_selector)

    # Extract text content if available and return as a list
    result = [element.get_text(strip=True) for element in elements]
    # print(result)
    # Return the element at the specified index if it exists
    return result[index] if len(result) > index else None


def extract_line_after_date(text):
    # Define a regex pattern to capture dates with or without ordinal indicators
    date_pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(?:st|nd|rd|th)?, \d{4}\b'

    # Find the date in the text
    date_match = re.search(date_pattern, text)

    if date_match:
        # Start searching for the line after the date
        start_pos = date_match.end()
        # Look for the first sentence (up to a period) after the date
        following_line_pattern = r'[^.]+\.'
        following_line_match = re.search(following_line_pattern, text[start_pos:])

        if following_line_match:
            return following_line_match.group(0).strip()  # Return the line after the date

    return None


# def get_all_rows(web_content, xpath):
#     tree = html.fromstring(web_content.content)
#
#     # Use XPath to extract all <tr> elements in the table
#     rows = tree.xpath(xpath)
#     # Print each row separately
#     for row in rows:
#         row_content = row.xpath('.//text()')  # Extract all text within the <tr>
#         row_content = [text.strip() for text in row_content if text.strip()]  # Clean and remove empty text
#         yield row_content


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
        row_data = {header: kwargs.get(header, 'N/A') for header in headers}
        writer.writerow(row_data)

    print(f"Data added to '{filename}' successfully!")


def extract_date(text):
    # Define a regex pattern to match dates like "July 13, 2016" or "July 7th, 2023"
    date_pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(?:st|nd|rd|th)?, \d{4}\b'

    # Search for the pattern in the text
    dates = re.findall(date_pattern, text)

    return dates



def creditform_info_2():
    url = "https://www.northdata.com/German+Deep+Tech+Quantum+2140+Verm%C3%B6gensverwaltungsgesellschaft+mbH"

    return requests.request("GET", url)


def get_attr_bs4(web_content, selector, attr):
    # Ensure we pass HTML content (string) instead of a Response object
    if hasattr(web_content, 'content'):
        web_content = web_content.content  # Get the HTML content as bytes

    # Parse the HTML content
    soup = BeautifulSoup(web_content, 'html.parser')

    # Use BeautifulSoup to select elements based on the selector
    elements = soup.select(selector)

    # Retrieve the data-id attribute for each matching element
    result = [element.get(attr) for element in elements if element.has_attr(attr)]
    # print(result)
    if result:
        return result[0]
    return 'N/A'



def subsidiaries_info(id):

    url = "https://www.northdata.com/data.json"

    payload = f"{{\"options\":[{{\"rootColor\":\"#66afac\",\"highlightBgColor\":\"#f3f4f5\",\"language\":\"en\",\"minHeight\":\"300\",\"width\":798,\"companyClick\":null,\"maxItems\":10,\"domain\":\"company\",\"id\":{id},\"layout\":\"graph\",\"ratio\":\"0.40\",\"type\":\"graph\",\"immediate\":true}}],\"origin\":\"www.northdata.com\",\"v\":\"1.196.48\"}}"
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://www.northdata.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.northdata.com/',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    return [name.get("query", {}).get("name") for name in data.get("result")[0].get("nodes")]


def get_hrefs(web_content, path):
    # Parse the HTML content
    soup = BeautifulSoup(web_content, 'html.parser')

    # Use the CSS selector to find all <a> tags within the specified <div>
    hrefs = [a['href'] for a in soup.select(path) if a.has_attr('href')]

    return hrefs

def is_number(value):
    # Check if value is a number (int or float)
    if isinstance(value, (int, float)):
        return True
    # Check if value is a string that can be converted to a number
    if isinstance(value, str):
        # Check for cases where the string can be considered a valid number
        # For example, allow multiple decimal points in a specific format
        if value.count('.') > 1:
            return True  # Accept strings like "10.5.0" as valid
        try:
            float(value)  # Attempt to convert the string to a float
            return True
        except ValueError:
            return False
    return False