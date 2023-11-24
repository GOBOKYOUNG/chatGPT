import openai
from telegram import ForceReply, Update
from telegram.ext import Application, MessageHandler, filters

def chatGPT(prompt):
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    result = completion.choices[0].message.content
    return result

# Telegram 봇 코드
token = "6486863471:AAFrifp_oH40to4f2GXuz0uQ1LJwQ4MV8_M"

async def gpt(update, context):
    prompt = update.message.text
    gpt_result = chatGPT(prompt)
    await update.message.reply_text(gpt_result)

def main():
    app = Application.builder().token(token).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gpt))

    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
