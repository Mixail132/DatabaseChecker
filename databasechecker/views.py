from connections import cursor
import requests
import time

prompt = """ 
Прочитай текст вакансии и определи относится ли он к backend разработке? 
Ответь пожалуйста да или нет?
"""


def make_sql():
    request = """ SELECT body FROM backend LIMIT 10"""
    cursor.execute(request)
    return cursor.fetchall()


def ask_gpt(vacancy):
    url = "https://mixail132.pythonanywhere.com/askgpt"
    data = {"question": f"{prompt} Текст вакансии: '{vacancy}'"}
    response = requests.post(url=url, json=data)
    answer = response.json()
    # print(answer)
    return answer['answer']


if __name__ == "__main__":
    all_vacancies = make_sql()
    for vacancy_text in all_vacancies:
        time.sleep(10)
        print((ask_gpt(vacancy_text[0])))
