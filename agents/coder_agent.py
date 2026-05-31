from utils.llm import llm

def coder_agent(plan):

    prompt = f"""
You are a Python coding assistant.

STRICT RULES:
- Return ONLY Python code
- No explanations
- No comments
- No docstrings
- No examples
- No main function
- No markdown
- No extra text

Output must be ONLY code.

Task:
{plan}
"""

    response = llm.invoke(prompt)
    return response.content.strip()