mkdir -p ~/.local/bin/
cp ./diral.py ~/.local/bin/diral
# cp ./diral ~/.local/bin/diral

if [[ ":$PATH:" != *"/.local/bin"* ]]; then
  echo 'export PATH=~/.local/bin:$PATH' >> ~/.bashrc
  echo 'export PATH=~/.local/bin:$PATH' >> ~/.zshrc
fi

