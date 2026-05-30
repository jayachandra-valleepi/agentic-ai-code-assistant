
# Root Files
touch app.py
touch requirements.txt
touch Dockerfile
touch docker-compose.yml
touch .env
touch README.md
touch .gitignore

# GitHub Workflow
mkdir -p .github/workflows
touch .github/workflows/deploy.yml

# Agents
mkdir -p agents
touch agents/planner_agent.py
touch agents/coder_agent.py
touch agents/reviewer_agent.py
touch agents/debugger_agent.py
touch agents/memory_agent.py

# Workflows
mkdir -p workflows
touch workflows/coding_workflow.py

# Tools
mkdir -p tools
touch tools/file_reader.py
touch tools/file_writer.py
touch tools/terminal_tool.py
touch tools/code_executor.py

# Utils
mkdir -p utils
touch utils/llm.py
touch utils/prompts.py

# Memory
mkdir -p memory
touch memory/chat_memory.py

# Templates
mkdir -p templates
touch templates/index.html

# Static
mkdir -p static
touch static/style.css
touch static/script.js

# Workspace
mkdir -p workspace/generated_code

echo "✅ AI Coding Assistant project structure created successfully!"