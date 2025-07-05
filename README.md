
# Протокол 13 - Агент Голосовых Идей

### Что это?
Это Telegram-бот, который принимает текст (или голос -> текст через Telegram), и отправляет идею в Notion-базу.

### Развёртка

1. Создай базу в [Notion](https://notion.so) — добавь колонку "Name" (тип: Title)
2. Создай Telegram-бота через @BotFather
3. Перейди на [Render.com](https://render.com)
4. Создай новый Web Service → залей этот архив или подключи GitHub
5. Введи 3 переменные окружения:
   - `NOTION_TOKEN` — из [Notion Integrations](https://www.notion.so/my-integrations)
   - `NOTION_DATABASE_ID` — ID базы, куда кидать текст
   - `TELEGRAM_TOKEN` — токен бота

### Готово! Теперь ты можешь слать текст боту — он будет появляться в Notion
