from utils.llm import llm

def planner_agent(user_query):

    prompt = f"""
You are an AI software architect.

Convert the request into a STRICT step list.

RULES:
- Only steps (max 5)
- Each step must be 1 short line
- No explanation
- No introduction
- No conclusion
- No paragraphs
- No extra text

FORMAT:
1. ...
2. ...
3. ...
4. ...
5. ...

User Request:
{user_query}
"""

    response = llm.invoke(prompt)
    return response.content.strip()