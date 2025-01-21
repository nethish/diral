mkdir -p ~/.local/bin/
cp ./diral.py ~/.local/bin/diral

if [[ ":$PATH:" != *"/.local/bin"* ]]; then
  echo 'export PATH=~/.local/bin:$PATH' >> ~/.bashrc
  echo 'export PATH=~/.local/bin:$PATH' >> ~/.zshrc
fi

cat ./cd >> ~/.bashrc
cat ./cd >> ~/.zshrc
