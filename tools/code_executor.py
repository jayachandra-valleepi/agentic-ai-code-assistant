import subprocess

def execute_python_file(file_path):
    result = subprocess.run(
        ["python", file_path],
        capture_output=True,
        text=True
    )


    return result.stdout