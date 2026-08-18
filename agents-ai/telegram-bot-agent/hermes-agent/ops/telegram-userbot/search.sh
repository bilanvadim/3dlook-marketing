#!/bin/bash
# Wrapper для быстрого вызова поиска
export TG_API_ID="${TG_API_ID:-12345}"
export TG_API_HASH="${TG_API_HASH:-placeholder}"
cd @HOME@/.hermes/telegram-userbot
exec python3 search.py "$@"
