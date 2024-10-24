import requests
from lxml import html


def scrape_ids(url, xpath_expression):
    """
    Scrapes IDs from a webpage using lxml and XPath.

    Parameters:
    - url (str): The URL of the webpage to scrape.
    - xpath_expression (str): The XPath expression to locate the IDs.

    Returns:
    - List of IDs found on the webpage.
    """
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'timezoneoffset=-300; timezonename=Asia/Karachi; _ga=GA1.1.1895846966.1728287506; _ga_J3M3WZB5B6=GS1.1.1728293543.2.0.1728293543.0.0.0; axeptio_cookies={%22$$token%22:%22m20ermecw7jm5wty0saei%22%2C%22$$date%22:%222024-10-17T05:13:26.819Z%22%2C%22$$cookiesVersion%22:{}%2C%22$$completed%22:false}; axeptio_authorized_vendors=%2C%2C; axeptio_all_vendors=%2C%2C; route=1729506540.021.2307.285880|1ca372b33d2bad9524c20eaf607b64ca; JSESSIONID=71D378AE7FBE3687A868C1FA184C0ECA; _k_cty_lang=es_ES; ROUTEID=.; timezoneoffset=-300; timezonename=Asia/Karachi; kp_uuid=e800a76b-6a08-441f-9d4f-a7284fa60b1a; _ga_H9RY6SXL1H=GS1.1.1729506543.5.1.1729506815.0.0.0; _ga_YFM4S8XBVP=GS1.1.1729506543.5.1.1729506815.60.0.457085426; _ga_LXLJM68PCS=GS1.1.1729506543.3.1.1729506815.0.0.0; datadome=fC3PdtjW2LWWvWSgVMSgZyRm6z1_XreGWx_sVhfaPdSHtvQw29lzJdPbmcgfXCoxFgpxqsd8_IJf4ulmjhEkxSua~e_bSA4vlZyJWFg8qSQLJsoVlT~yDZD9Q1WNHNey',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-device-memory': '8',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="129.0.6668.101", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the HTML content using lxml
        tree = html.fromstring(response.content)

        # Use the XPath expression to extract the IDs
        ids = tree.xpath(xpath_expression)

        # Return the list of IDs
        return ids
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []


# Example usage
url = 'https://es.kompass.com/businessplace/z/de/page-1/'
xpath_expression = "//div[@class='resultatDivId']/div/@id"
# Adjust this XPath based on the structure of the target page

ids = scrape_ids(url, xpath_expression)

if ids:
    print("Scraped IDs:")
    for entity_id in ids:
        print(scrape_ids(url, f"//div[@class='resultatDivId']/div//a[@id='seoCompanyLinkD{entity_id.split("D")[1]}']/@href"))

else:
    print("No IDs found.")
