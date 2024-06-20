import telebot
import openai

bot = telebot.TeleBot ('telegramapino') 

openai.api_key = 'chatgptapino'

def generate_answer(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": text},
            ]
        )

        result = ''
        for choice in response.choices:
            result += choice.message.content

    except Exception as e:
        return f"Oops!! openAI Sorun Var. Sebep: {e}"

    return result


@bot.message_handler(content_types=['text'])
def send_text(message):
    answer = generate_answer(message.text)
    bot.send_message(message.chat.id, answer)

bot.polling()
