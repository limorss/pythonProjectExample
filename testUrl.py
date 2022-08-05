import requests


WORLD_UNIVERSITIES_URL = "http://universities.hipolabs.com/search?country="
REST_API_SUCCESS_RESPONSE = 200


def check_country_universities_num_exists(num_of_universities, country):
    try:
        universities_response = requests.get(f"{WORLD_UNIVERSITIES_URL}{country}")
        if 200 == universities_response.status_code:
            assert len(universities_response.json()) >= num_of_universities
            print(f"At  least {num_of_universities} universities exists in {WORLD_UNIVERSITIES_URL}{country}")
    except TypeError as e:
        print(f"Type Error Exception occurred (wrong parameter type), see more details here: {e.args}")
