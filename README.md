# Life OS — база знаний

Мануалы по Life OS для человека и его агента (Claude Code, Codex): установка, входящие из Telegram и почты, документы
по шаблонам, сайт. Сайт: https://antonlozhkin.ru/lifeos-docs/

Собрано на шаблоне [np-template-docs](https://github.com/cookiespooky/np-template-docs) движка
[Notepub](https://antonlozhkin.ru/np/ru/). Репозиторий сам — шаблон: **Use this template**, и у вас та же база знаний
для своего продукта или дела.

## Как устроено

| что | где |
|---|---|
| разделы | `content/<раздел>/<раздел>.md` (`type: hub`; имя файла — адрес раздела, не `index.md`: два `index.md` конфликтуют) |
| мануалы | `content/<раздел>/<адрес>.md` (`type: article`, `hub: ["<раздел>"]`, `order`) |
| главная, поиск, подвал | `content/home.md`, `content/search.md`, `content/footer.md` |
| название, логотип, цвет | `Site.md`; подписи интерфейса — `Interface.md` |
| техника: тема, правила, сборка | `.np/` — менять не нужно |

Мануал пишется по одной схеме: **что делает · что нужно · как включить · как пользоваться** (фразы агенту и
команды) **· если не работает · где данные**. Пишется только по тому, что работает, и проверяется проходом на чистой
установке.

## Сборка

```bash
NOTEPUB_BIN=/path/to/notepub ./.np/scripts/preview.sh   # собрать и открыть http://127.0.0.1:8080/
NOTEPUB_BIN=/path/to/notepub ./.np/scripts/build.sh     # только собрать в .np/dist/
```

Пуш в `main` публикует сайт на GitHub Pages (`.github/workflows/`).
