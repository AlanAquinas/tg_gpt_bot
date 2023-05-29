import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



token = '6206483462:AAFTexy0r51Wzyk5DqTjTPdhOoAWfhFzCCI'
openai.api_key = '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'


bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You:"]
    )
    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)


