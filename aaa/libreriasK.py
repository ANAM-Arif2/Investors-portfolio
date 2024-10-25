from utils import kompass_info, get_content, extract_date, get_all_rows, translate_text_auto, create_csv_with_headers, kompass_info_2
from googletrans import Translator

translator = Translator()

headers = ["cik", "entity_id", 'entityType', 'sic', 'sicDescription', 'name', 'tickers', 'exchanges', 'ein', 'description', 'website', 'investorWebsite', 'category', 'fiscalYearEnd', 'stateOfIncorporation', 'stateOfIncorporationDescription', 'Address', 'phone', 'formerNames', 'Location', 'creation', 'capital', 'Employees']


def scrapping():
    web_content = kompass_info()
    web_content_2 = kompass_info_2()

    entity_id = get_content(web_content, "//div[@id='identifikationsdaten']/div/div[2]//p[@class='mb-0']/span")
    # entity_id = next(entity_id)
    entity_id = entity_id[0]

    name = get_content(web_content, "//h1/span")
    name = name[0]


    # name = translate_text_auto(next(name), "en")
    # print(name)
    # # print(translator.translate(next(name)))
    sicDescription = get_content(web_content, "//div[@id='branche']//p[@class]/span[2]")[0]
    print(sicDescription)
    description = get_content(web_content, "//div[@id='firmenauskunft']//p/span[1]")[0]
    print(description)
    # sicDescription = translate_text_auto(next(sicDescription), "en")
    sic = get_content(web_content, "//div[@id='branche']//p[@class='mb-0']/span")[0]
    print(sic)
    website = get_content(web_content, "//div[@id='kontakt']/div[@class='content']//a[contains(@class, 'text-white')]")
    if website:
        website = website[0]
    else:
        website = "N/A"
    # print(website[0])
    category = sicDescription
    stateOfIncorporation = "Germany"
    fiscalYearEnd = extract_date(translate_text_auto(get_content(web_content, "//div[@id='firmenauskunft']//p")[1], "en"))
    print(fiscalYearEnd)
    if fiscalYearEnd:
        fiscalYearEnd = fiscalYearEnd[0]
    address = get_content(web_content, "//div[@id='kontakt']/div[@class='content']//p[contains(@class, 'text-white')]/span")
    # address = translate_text_auto(address, "en")
    # print(' '.join(address))
    # location = get_content(web_content, "//p[@class='blockAddress flagWorld']/span[2]")
    # location = translate_text_auto(next(location), "en")
    # print(location)
    phone = get_content(web_content, "//div[@id='kontakt']/div[@class='content']//p[contains(@class, 'adres-white')]/span")
    if phone:
        phone = phone[0]
    else:
        phone = 'N/A'
    # print(phone[0])
    formerNames = get_content(web_content_2, "//div[@class='former item']/div[@class='content']")
    # formerNames = next(formerNames)
    if formerNames:
        formerNames = formerNames[0]
    else:
        formerNames = 'N/A'
    # employees = get_all_rows(web_content, "//table[@class='tableInfoJuridic']")
    # employees = next(employees)[-4:]
    # print(employees)
    # management = None
    # staff = None
    # if 'Personal' in employees[0]:
    #     management = employees[1]
    # if employees[2] == "Personal de la empresa":
    #     staff = employees[3]
    # management_staff = translate_text_auto(f"{management}, {staff}", "en")
    # print(management_staff)
    create_csv_with_headers('scraped_info.csv', headers, cik=entity_id, entity_id=entity_id, name=name, category=category, stateOfIncorporation=stateOfIncorporation, fiscalYearEnd=fiscalYearEnd, sicDescription=sicDescription, website=website, Address=' '.join(address), phone=phone, formerNames=formerNames)

