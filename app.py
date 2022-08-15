import argparse
import base64
import os
from pathlib import Path
from io import BytesIO
import time
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from consts import DEFAULT_IMG_OUTPUT_DIR
from utils import parse_arg_boolean, parse_arg_dalle_version
from consts import ModelSize

app = Flask(__name__)
CORS(app)
print("--> Starting DALL-E Server. This might take up to two minutes.")
from dalle_model import DalleModel

##################################
#Parameters

#choose with mini (4GB of vram), mega (8GB of vram), mega_full (12 or 16 GB of vram, need a very strong GPU, Nvidia Tesla T4 from AWS g4dn family instance is okay, approx 15sec per images)
dalle_model = DalleModel("mini") 
text_prompt = "An apple fighting a potato"
num_images = 4

###################################
if os.path.exists('generated_imgs')  == False:
        os.mkdir("generated_imgs")

#result is a list
generated_imgs = dalle_model.generate_images(text_prompt, num_images)

for idx, img in enumerate(generated_imgs):
        img.save(os.path.join("generated_imgs/", f'{idx}.jpeg'), format='JPEG')
