<p align="center">
<img src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/woman-artist_1f469-200d-1f3a8.png" width="60" alt="Dali">
  <h2 align="center">DALL-E Playground</h2>
</p>

<h2>Installation</h2>

First, clone this repo, you can also download the zip\n
`git clone https://github.com/razor11800/dalle-playground.git`

Optionnal : install CUDA if it's not already done\n
`sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
sudo apt-get update
sudo apt install cuda=11.6.2-1`

Install ubuntu packages\n
`sudo apt install python3-pip python3`

Install python packages dependancies\n
`pip3 install -r requirements.txt
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
pip3 install "jax[cuda]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
