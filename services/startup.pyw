import subprocess
import os
import time

def run_in_background(command, cwd=None):
    """Run a command in the background without opening a new window."""
    subprocess.Popen(command, cwd=cwd, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)

# Paths to backend and frontend directories
backend_dir = r"C:\Getin\skf_mys\backend"
frontend_dir = r"C:\Getin\skf_mys\frontend\sakai-ng"

# Activate virtual environment and run backend commands
activate_venv_command = r"venv\Scripts\activate && "
backend_commands = [
    "python manage.py runserver 0.0.0.0:8000",
    "celery -A backend worker",
    "celery -A backend beat"
]

# Run backend deployment
for command in backend_commands:
    full_command = activate_venv_command + command
    run_in_background(full_command, cwd=backend_dir)

# Run frontend command
frontend_command = ["ng", "serve", "--host", "0.0.0.0", "--disable-host-check"]
run_in_background(frontend_command, cwd=frontend_dir)

print("Deployment started in the background.")
