import subprocess

subprocess.call(["apt install git", "-la"], shell=True)

subprocess.call(["apt update", "-la"], shell=True)

subprocess.call(["apt upgrade", "-la"], shell=True)

subprocess.call(["apt install nano", "-la"], shell=True)

subprocess.call(["apt install wget", "-la"], shell=True)

subprocess.call(["apt install python", "-la"], shell=True)

subprocess.call(["apt install termux-tools", "-la"], shell=True)

subprocess.call(["apt install php", "-la"], shell=True)

subprocess.call(["pkg install unstable-repo", "-la"], shell=True)

subprocess.call(["pkg install coreutils", "-la"], shell=True)

subprocess.call(["apt install curl", "-la"], shell=True)
