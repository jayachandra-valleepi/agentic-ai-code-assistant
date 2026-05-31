from agents.planner_agent import planner_agent
from agents.coder_agent import coder_agent
from agents.reviewer_agent import reviewer_agent
from agents.memory_agent import save_memory


def run_agentic_workflow(user_query):

    plan = planner_agent(user_query)
    generated_code = coder_agent(plan)
    review = reviewer_agent(generated_code)

    is_simple = len(user_query.split()) < 12

    # SIMPLE CASE → ONLY CODE
    if is_simple:
        final_response = f"""
{generated_code}
"""
    else:
        # COMPLEX CASE → FULL VIEW
        final_response = f"""
===========================
GENERATED CODE
===========================

{generated_code}
"""

        if review != "OK":
            final_response += f"""

===========================
CODE REVIEW
===========================

{review}
"""

    save_memory(user_query, final_response)
    return final_response