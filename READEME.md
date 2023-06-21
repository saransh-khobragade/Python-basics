## Install python 

brew install pyenv
pyenv install 3.9.2 

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc

pyenv global 3.9.2

pyenv versions

restart terminal
 
python