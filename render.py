services:
  - type: web
    name: Text Leech Bot
    plan: free
    env: docker
    dockerfilePath: Dockerfile
    repo: https://github.com/AshutoshGoswami24/text-leech-bot-for-render
    branch: main
    autoDeploy: false
    envVars:
      - key: BOT_TOKEN
        sync: false
      - key: API_ID
        sync: false
      - key: API_HASH
        sync: false
      - key: WEBHOOK
        sync: false
      - key: PORT
        sync: false  # Default port value, update if needed￼Enter
