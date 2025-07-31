sudo apt update
sudo apt install python3-pip
sudo rm /usr/lib/python3.12/EXTERNALLY-MANAGED 
pip3 install -r requirements.txt 
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:1b
pip install ollama
