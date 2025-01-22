mkdir -p ~/.local/bin/
chmod +x ./saila.py
cp ./saila.py ~/.local/bin/saila

if [[ ":$PATH:" != *"/.local/bin"* ]]; then
  echo 'export PATH=~/.local/bin:$PATH' >> ~/.bashrc
  echo 'export PATH=~/.local/bin:$PATH' >> ~/.zshrc
fi

cat ./cd >> ~/.bashrc
cat ./cd >> ~/.zshrc
