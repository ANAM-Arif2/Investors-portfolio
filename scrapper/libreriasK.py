from utils import creditform_info, is_number, subsidiaries_info, get_content_bs4, get_attr_bs4, extract_line_after_date, \
    extract_date, translate_text_auto, create_csv_with_headers, creditform_info_2
from googletrans import Translator

translator = Translator()

headers = ["cik", "entity_id", 'entityType', 'sic', 'sicDescription', 'name', 'tickers', 'exchanges', 'ein',
           'description', 'website', 'investorWebsite', 'category', 'fiscalYearEnd', 'stateOfIncorporation',
           'stateOfIncorporationDescription', 'Address', 'phone', 'formerNames', 'subsidiaries', 'Location', 'creation',
           'capital', 'Employees']


def scrapping():
    web_content = creditform_info()
    web_content_2 = creditform_info_2()

    entity_id = get_content_bs4(web_content, "#identifikationsdaten > div > div:nth-of-type(2) .mb-0 > span", index=1)
    # print(entity_id)
    # entity_id = get_content(web_content, "#identifikationsdaten > div > div:nth-of-type(2) p.mb-0 > span", index=0)
    # entity_id = next(entity_id)
    # entity_id = entity_id[0]
    #
    name = get_content_bs4(web_content, "h1 > span", index=0)
    # print(name)
    # name = name[0]

    # name = translate_text_auto(next(name), "en")
    # print(name)
    # # print(translator.translate(next(name)))
    sicDescription = get_content_bs4(web_content, "#branche p[class] > span:nth-of-type(2)", index=0)
    # print(sicDescription)
    sicDescription = translate_text_auto(sicDescription, 'en')
    description = get_content_bs4(web_content, "div#firmenauskunft div p", index=1)
    description = translate_text_auto(description, 'en')
    print(description)
    # print("description", description)
    # # sicDescription = translate_text_auto(next(sicDescription), "en")
    sic = get_content_bs4(web_content, "#branche div p > span", index=0)
    if not is_number(sic):
        sic = get_content_bs4(web_content, "#branche div p > span", index=1)
    if not is_number(sic):
        sic = get_content_bs4(web_content, "#branche div p > span", index=2)
    if not is_number(sic):
        sic = get_content_bs4(web_content, "#branche div p > span", index=3)
    print(sic)
    website = get_content_bs4(web_content, "#kontakt > div.content a.text-white")
    if not website:
        website = "N/A"
    # # print(website[0])
    category = sicDescription
    stateOfIncorporation = "Germany"
    translated_para = translate_text_auto(get_content_bs4(web_content, "#firmenauskunft p", index=1), "en")
    fiscalYearEnd = extract_date(translated_para)
    print(fiscalYearEnd)
    if fiscalYearEnd:
        fiscalYearEnd = fiscalYearEnd[0]
    else:
        fiscalYearEnd = 'N/A'
    address = get_content_bs4(web_content, "#kontakt > div.content p.text-white > span", index=0)
    Location = get_content_bs4(web_content_2, "div.general-information.ui.relaxed.list a", index=1)
    if not Location or not 'Germany' in Location:
        Location = get_content_bs4(web_content_2, "div.general-information.ui.relaxed.list a", index=0)
    # # print(' '.join(address))
    # # location = get_content(web_content, "//p[@class='blockAddress flagWorld']/span[2]")
    # # location = translate_text_auto(next(location), "en")
    # # print(location)
    phone = get_content_bs4(web_content, "#kontakt > div.content p[class*='adres-white'] > span")
    if not phone:
        phone = 'N/A'

    id = get_attr_bs4(web_content_2, 'figure.bizq', 'data-id')
    # print(id)
    subsidiaries_info_value = subsidiaries_info(id)
    subsidiaries = ", ".join(str(item) if item is not None else '' for item in subsidiaries_info_value)
    # print(subsidiaries)
    # print(phone[0])
    formerNames = get_content_bs4(web_content_2, "div.former.item > div.content")
    # formerNames = next(formerNames)
    # if formerNames:
    #     formerNames = formerNames[0]
    # else:
    #     formerNames = 'N/A'
    employees = extract_line_after_date(translated_para)
    # print("-----------------", employees)

    # # employees = next(employees)[-4:]
    # # print(employees)
    # # management = None
    # # staff = None
    # # if 'Personal' in employees[0]:
    # #     management = employees[1]
    # # if employees[2] == "Personal de la empresa":
    # #     staff = employees[3]
    # # management_staff = translate_text_auto(f"{management}, {staff}", "en")
    # # print(management_staff)
    create_csv_with_headers('scraped_info.csv', headers, cik=entity_id, subsidiaries=subsidiaries, entity_id=entity_id,
                            sic=sic, name=name, category=category, stateOfIncorporation=stateOfIncorporation,
                            fiscalYearEnd=fiscalYearEnd, sicDescription=sicDescription, website=website,
                            Address=' '.join(address), Employees=employees, Location=Location, phone=phone,
                            formerNames=formerNames, description=description)
