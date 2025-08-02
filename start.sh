sudo apt update
sudo apt install python3-pip
sudo rm /usr/lib/python3.12/EXTERNALLY-MANAGED 
pip3 install -r requirements.txt 
curl -fsSL https://ollama.com/install.sh | sh
pip install ollama
sudo apt install uvicorn
ollama pull llama3.2:1b
ollama pull qwen2.5:1.5b
uvicorn main:app --host 0.0.0.0 --port 8080
