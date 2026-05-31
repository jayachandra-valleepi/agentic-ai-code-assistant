from utils.llm import llm

def debugger_agent(error_message):

    prompt = f"""
You are a Python debugging assistant.

STRICT RULES:
- Be very concise
- No long explanation
- No theory
- No extra context
- Only output:

1. ERROR CAUSE (1 line)
2. FIX (short code or instruction)

If possible, provide corrected code.

Error:
{error_message}
"""

    response = llm.invoke(prompt)
    return response.content.strip()