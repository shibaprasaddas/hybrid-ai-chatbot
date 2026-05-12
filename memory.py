# Simple memory placeholder

conversation_memory = []


def save_message(role, message):
    conversation_memory.append({
        "role": role,
        "message": message
    })


def get_memory():
    return conversation_memory
