import openai
from dotenv import load_dotenv
import os


def input_text():
    _prompt = input("Input your request here:\n")
    if _prompt:
        return _prompt
    else:
        input_text()


def text_format(text):
    words = text.split(' ')
    total_len = 0
    result_words = []
    for word in words:
        total_len += len(word)
        total_len += 1
        if total_len > 80:
            result_words.append('\n')
            total_len = 0
        result_words.append(word)
    return ' '.join(result_words)


def openai_init():
    load_dotenv()
    openai.organization = os.environ['GPT_organization']
    openai.api_key = os.environ['GPT_API_key']


def gpt_request(prompt):
    openai_init()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=128,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return text_format(response['choices'][0]['text'])


if __name__ == '__main__':
    while True:
        prompt = input_text()
        print('GPT response:')
        print(gpt_request(prompt))
        print('_'*80)

