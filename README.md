<p align="center">
  <h2 align="center">DALL-E Playground</h2>
</p>
<h2>prerequisites</h2>
Ubuntu LTS 20.04<br/>
A good Nvidia GPU with 4GB of VRAM minimum<br/>

<h2>Installation</h2>

First, clone this repo (you can also download the zip) and cd to the folder <br/>
`git clone https://github.com/razor11800/dalle-playground.git`<br/>
`cd dalle-playground`<br/>

Optionnal : install CUDA if it's not already done <br/>
`sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub`<br/>
`wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin`<br/>
`sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600`<br/>
`sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"`<br/>
`sudo apt-get update`<br/>
`sudo apt install cuda=11.6.2-1`<br/>
Restart you workstation <br/><br/>
Install ubuntu packages<br/>
`sudo apt install python3-pip python3`<br/>

Install python packages dependancies<br/>
`pip3 install -r requirements.txt`<br/>
`pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116`<br/>
`pip3 install "jax[cuda]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html`

<h2>How to run it</h2>

in the file `app.py`, you can edit 3 parameters line 21 22 23 :<br/>
Replace `<model>` by mini (4GB of VRAM recommended) mega (8GB of VRAM recommended) or mega_full (12GB of VRAM recommended, work on g4dn AWS instances)<br/>
`dalle_model = DalleModel("<model>")` <br/>
Replace `<prompt text>` by whatever you want to generate<br/>
`text_prompt = "<prompt text>"`<br/>
Replace `<image ammount>`by the amount of images you want to generate<br/>
`num_images = <image ammount>`<br/><br/>

Sample parameters:<br/><br/>
`dalle_model = DalleModel("mini")` <br/>
`text_prompt = "An apple fighting a potato"`<br/>
`num_images = 4`

after that, simply run `python3 app.py`<br/>
You will find your generated images in the folder `generated_imgs`<br/><br/>

That's it !
