import re


def extract_date(text):
    # Define a regular expression pattern for dates like "July 13, 2016"
    date_pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}\b'

    # Search for the pattern in the text
    dates = re.findall(date_pattern, text)

    return dates


# Example usage
text = """German Deep Tech Innovations AG, based in Potsdam, is registered in the commercial register with the legal form of a stock corporation. The company is registered with the local court in 14467 Potsdam under the commercial register number HRB 26342 P. The company is economically active. The last change in the commercial register was made on July 13, 2016. The company is currently managed by 4 managers (1 x board member, 3 x supervisory board members). There is one shareholder involved in the company. The company's VAT ID is available in the company data. The company has one location."""

extracted_dates = extract_date(text)
print(extracted_dates)
