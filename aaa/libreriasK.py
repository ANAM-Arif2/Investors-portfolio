from utils import kompass_info, get_content, get_all_rows, translate_text_auto, create_csv_with_headers
from googletrans import Translator

translator = Translator()

headers = ["entity_id", 'entityType', 'sic', 'sicDescription', 'name', 'description', 'website', 'category', 'stateOfIncorporation', 'stateOfIncorporationDescription', 'Address', 'phone', 'Location', 'Employees']


def scrapping():
    web_content = kompass_info()
    entity_id = get_content(web_content, "//div[@id='identifikationsdaten']/div/div[2]//p[@class='mb-0']/span")
    entity_id = next(entity_id)
    print(entity_id)

    name = get_content(web_content, "//h1/span")
    print(next(name))


    # name = translate_text_auto(next(name), "en")
    # print(name)
    # # print(translator.translate(next(name)))
    # sicDescription = get_content(web_content, "//p[@class='detailSlogan']")
    # sicDescription = translate_text_auto(next(sicDescription), "en")
    # print(sicDescription)
    # website = get_content(web_content, "//tr[@class='trWebSite']/td/a")
    # website = next(website)
    address = get_content(web_content, "//div[@id='kontakt']/div[@class='content']//p[contains(@class, 'text-white')]/span")
    address = translate_text_auto(next(address), "en")
    print(address)
    # location = get_content(web_content, "//p[@class='blockAddress flagWorld']/span[2]")
    # location = translate_text_auto(next(location), "en")
    # print(location)
    phone = get_content(web_content, "//div[@id='kontakt']/div[@class='content']//p[contains(@class, 'adres-white')]/span")
    phone = next(phone)
    print(phone)
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
    # create_csv_with_headers('scraped_info.csv', headers, entity_id=entity_id, name=name, sicDescription=sicDescription, website=website, Address=address, phone=phone, Employees=management_staff, Location=location)

