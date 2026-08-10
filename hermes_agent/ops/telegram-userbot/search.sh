#!/bin/bash
# Wrapper для быстрого вызова поиска
export TG_API_ID="${TG_API_ID:-12345}"
export TG_API_HASH="${TG_API_HASH:-placeholder}"
cd /home/vadim_prod/.hermes/telegram-userbot
exec python3 search.py "$@"
