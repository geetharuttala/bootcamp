MAX_RETRIES = 3

def connect_to_service():
    for attempt in range(MAX_RETRIES):
        print(f"Attempt {attempt + 1}")
        # simulate attempt
connect_to_service()
