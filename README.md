# MCP Gateway

Простой MCP Gateway, который даёт HTTP‑доступ к набору MCP‑инструментов через единый REST API.

Прод:  
`https://mcp-gateway-ytlz.onrender.com`

## Что это

MCP Gateway — это тонкий слой между AI‑клиентами (Claude, Cursor, кастомные агенты) и MCP‑серверами.  
Он предоставляет единый HTTP‑endpoint, авторизацию по API‑ключу и стабильный URL, чтобы не поднимать MCP‑серверы локально на каждой машине.

Основной use case сейчас:

> Удалённая MCP‑точка для разработчика или небольшой команды, которая хочет дергать файловые и утилитарные инструменты из ИИ, не поднимая у себя Node/Docker/серверы.

## Быстрый старт

### Health‑чек

curl https://mcp-gateway-ytlz.onrender.com/health

→ {"status":"ok"}
text

### Список доступных инструментов

curl "https://mcp-gateway-ytlz.onrender.com/api/tools"
-H "x-api-key: demo-key-123"

→ {"tools":["filesystem/list","calculator/add"]}
text

### Вызов инструмента

Пока реализованы заглушки для примера интеграции.

curl -X POST
"https://mcp-gateway-ytlz.onrender.com/api/tools/filesystem/list"
-H "x-api-key: demo-key-123"
-H "Content-Type: application/json"
-d '{"path": "/"}'

text

Ответ (пример):

{
"result": "filesystem/list executed",
"data": {
"path": "/"
}
}

text

Аналогично для `calculator/add`:

curl -X POST
"https://mcp-gateway-ytlz.onrender.com/api/tools/calculator/add"
-H "x-api-key: demo-key-123"
-H "Content-Type: application/json"
-d '{"a": 1, "b": 2}'

text

---

## Архитектура (упрощённо)

- **FastAPI** — HTTP‑слой (`/health`, `/api/tools/...`).
- **API‑ключ** в заголовке `x-api-key` — простая аутентификация.
- За `/api/tools/{server}/{method}` сейчас стоят заглушки; следующая итерация — подключение реальных MCP‑серверов (filesystem, calculator и т.д.) через MCP‑клиент.

---

## Ограничения и SLA (ранний прототип)

- Сервис крутится на бесплатном инстансе Render; формального SLA и финансовых гарантий нет.  
- Возможны перезапуски и простой, поэтому не рекомендуется использовать для критичных прод‑нагрузок.  
- Публичный API может меняться, но breaking‑changes будут делать с предупреждением через релиз‑ноты/коммиты.

---

## Планы

- Подключить реальные MCP‑серверы (filesystem, GitHub и др.).
- Ввести отдельные API‑ключи на пользователя и простые лимиты.  
- Сделать минимальный тариф Pro для стабильного использования в командах.

---

## Связаться

Если хотите попробовать MCP Gateway в своём проекте или нужны доработки под ваш стек:

- Telegram: `@aerobiuse`
