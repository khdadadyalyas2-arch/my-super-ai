import os
from openai import OpenAI

# توکن مرحله اول رو بین دو کوتیشن بذار
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "توکن_خودت_رو_اینجا_پیست_کن")

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_TOKEN,
)

print("==================================================")
print("   ابر هوش مصنوعی اختصاصی فعال شد!               ")
print("   هر سوالی داری بپرس (برای خروج بنویس: exit)      ")
print("==================================================")

chat_history = [
    {
        "role": "system",
        "content": (
            "You are an uncensored, highly technical, and objective AI assistant specialized in Web3, "
            "smart contracts, blockchain security, Solidity, Python, and system architecture. "
            "Provide direct, complete, production-ready code and solutions. "
            "Do not include generic legal disclaimers, ethical lectures, or boilerplate warnings. "
            "Focus purely on technical implementation, logic, and developer needs. "
            "Always respond in fluent Persian unless asked otherwise."
        )
    }
]

while True:
    try:
        user_input = input("\nشما: ")
        if user_input.strip().lower() in ["exit", "خروج"]:
            print("خداحافظ رفیق!")
            break
        if not user_input.strip():
            continue

        chat_history.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            messages=chat_history,
            model="gpt-4o",
            temperature=0.7,
        )

        answer = response.choices[0].message.content
        print(f"\nابرهوش:\n{answer}")
        chat_history.append({"role": "assistant", "content": answer})

    except Exception as e:
        print(f"\nخطا: {e}")
