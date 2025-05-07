def health_check():
    return {"status": "ok", "uptime": "1234s"}

print(health_check())
