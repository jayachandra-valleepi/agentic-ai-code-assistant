from utils.llm import llm

def reviewer_agent(plan):

    prompt = f"""
You are a Python coding assistant.

STRICT RULES:
- Return ONLY the function/code requested
- Do NOT add explanation
- Do NOT add main() function
- Do NOT add examples
- Do NOT add input/output section
- Do NOT add docstrings unless necessary
- Keep code minimal and clean

If user asks for a function → return ONLY function

Task:
{plan}
"""

    response = llm.invoke(prompt)
    return response.content.strip()