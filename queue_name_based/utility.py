def message_handler(ch, mothod, properties, body):
    print(f"[*] message >> {body}")