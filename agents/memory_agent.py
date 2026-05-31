from memory.chat_memory import memory


def save_memory(user_input, ai_response):

    memory.save_context(
        {"input": user_input},
        {"output": ai_response}
    )


def load_memory():

    return memory.load_memory_variables({})