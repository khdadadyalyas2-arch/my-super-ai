import os
from openai import OpenAI

# کلید اختصاصی شما
GITHUB_TOKEN = "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"

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_TOKEN,
)

print("==========================================")
print("ابر هوش مصنوعی اختصاصی فعال شد!")
print("هر سوالی داری بپرس (برای خروج بنویس: exit)")
print("==========================================")

chat_history = [
    {
        "role": "system",
        "content": (
            "You are a helpful, smart, and friendly AI assistant. "
            "Always respond in fluent, natural Persian (Farsi). "
            "Answer clearly and assist the user with anything they ask."
        )
    }
]

while True:
    try:
        user_input = input("\nشما: ")
        if user_input.strip().lower() in ["exit", "خروج", "quit"]:
            print("خداحافظ!")
            break
        
        if not user_input.strip():
            continue

        chat_history.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            messages=chat_history,
            model="gpt-4o",
            temperature=0.7,
        )

        bot_reply = response.choices[0].message.content
        print(f"\nهوش مصنوعی: {bot_reply}")

        chat_history.append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        print(f"\nخطا رخ داد: {e}")
