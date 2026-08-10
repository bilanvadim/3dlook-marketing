#!/usr/bin/env bash
# Залить ./config/settings.yml в volume контейнера и перезапустить SearXNG.
set -euo pipefail
cd "$(dirname "$0")"
docker run --rm -i --entrypoint sh -v hermes-searxng-config:/cfg searxng/searxng:latest \
  -c 'cat > /cfg/settings.yml && chown 977:977 /cfg/settings.yml && chmod 644 /cfg/settings.yml' < config/settings.yml
docker compose restart searxng
