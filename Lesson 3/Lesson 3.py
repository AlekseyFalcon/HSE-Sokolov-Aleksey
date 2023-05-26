from lesson_2_data import courts, respondents


def make_court_nominative_case(court_name: str) -> str:
    words = court_name.split(" ")[2::]
    text = "Арбитражный суд"
    for i in words:
        text += f" {i}"
    return text


def task_2():
    def make_a_header(court, plaintiff, respondent):
        def make_person_info_str(person, title):
            name = person.get('name', '-')
            inn = person.get('inn', '-')
            ogrnip = person.get('ogrnip', '-')
            address = person.get('address', '-')
            person_info = f"""{title}: {name}
    ИНН {inn} ОГРНИП {ogrnip}
    Адрес: {address}\n"""
            return person_info

        court_name = make_court_nominative_case(court['name'])
        plaintiff_info = make_person_info_str(plaintiff, "Истец")
        respondent_info = make_person_info_str(respondent, "Ответчик")
        case_number = f"Номер дела {respondent['case_number']}"
        header = f"""-------------------------------
В {court_name}
Адрес: {court['address']}

{plaintiff_info}

{respondent_info}

{case_number}
"""
        return header

    plaintiff = {
        "name": "Соколов Алексей Васильевич",
        "inn": "9876543211",
        "ogrnip": "4567486473748",
        "address": "111111, г. Москва, ул. Каховка, 27"
    }

    cleaned_respondents = [i for i in respondents if i.get("case_number")]
    for respondent in cleaned_respondents:
        court_code = respondent["case_number"].split("-")[0]
        court = courts[court_code]
        header = make_a_header(court, plaintiff, respondent)
        print(header)