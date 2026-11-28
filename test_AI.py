import subprocess
result = subprocess.run(['claude', '-p', 'say hello'], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
