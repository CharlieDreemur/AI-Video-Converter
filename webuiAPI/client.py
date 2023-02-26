import webuiapi
import os
import datetime
from PIL import Image, PngImagePlugin
import json
import requests
import io
import base64
from io import BytesIO
# create API client
api = webuiapi.WebUIApi()

# create API client with custom host, port
api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)

# create API client with custom host, port and https
#api = webuiapi.WebUIApi(host='webui.example.com', port=443, use_https=True)

# create API client with default sampler, steps.
#api = webuiapi.WebUIApi(sampler='Euler a', steps=20)

# optionally set username, password when --api-auth is set on webui.
api.set_auth('username', 'password')

def txt2img(prompt_in="best quality, masterpiece, highly detailed, photo realisitc, cute, cat", styles_in=[],cfg_scale_in=7, seed_in=-1, sampler_index_in='EularA',step_in=20, denoising_strength_in=0.75):
    result = api.txt2img(prompt=prompt_in,
                    negative_prompt="(bad quality), (worst quality)",
                    seed=seed_in,
                    styles=styles_in,
                    cfg_scale=cfg_scale_in,
                       sampler_index=sampler_index_in,
                       steps=step_in,
#                      enable_hr=True,
#                      hr_scale=2,
#                      hr_upscaler=webuiapi.HiResUpscaler.Latent,
#                      hr_second_pass_steps=20,
#                      hr_resize_x=1536,
#                      hr_resize_y=1024,
                       denoising_strength=denoising_strength_in,

    )
    return result.image


url = "http://127.0.0.1:7860"
#Convert image to base64
def pil_to_base64(pil_image):
    with BytesIO() as stream:
        pil_image.save(stream, "PNG", pnginfo=None)
        base64_str = str(base64.b64encode(stream.getvalue()), "utf-8")
        return "data:image/png;base64," + base64_str


payload = {
    "prompt": "best quality, masterpiece, 1girl",
    #"negative_prompt": "",
    "steps": 30,
    "denoising_strength": 0.75,
    #"mask": "string",
    #"mask_blur": 4,
    #"inpainting_fill": 0,
    #"inpaint_full_res": True,
    #"inpaint_full_res_padding": 0,
    #"inpainting_mask_invert": 0,
    #"initial_noise_multiplier": 0,
    #"styles": ["string"],
    "seed": -1,
    "sampler_name": "Euler a",
    "cfg_scale": 12,
    "width": 512,
    "height": 512,
    #"restore_faces": False,
    #"tiling": False,
    #"override_settings": {},
    #"override_settings_restore_afterwards": True,
    #"include_init_images": False
}
def pil_to_base64(pil_image):
        with BytesIO() as stream:
            pil_image.save(stream, "PNG", pnginfo=None)
            base64_str = str(base64.b64encode(stream.getvalue()), "utf-8")
            return "data:image/png;base64," + base64_str
        
def img2img(image, payload):
    #Convert image to base64
    payload["init_images"] = [pil_to_base64(image)] #Plug converted Image to Payload

    response = requests.post(url=f'{url}/sdapi/v1/img2img', json=payload)
    r = response.json()
    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        return image

def controlNetImg2img(image):
    cn = webuiapi.ControlNetInterface(api)
    cn.model_list()
    print(cn.model_list())
    output = cn.img2img(prompt="best quality, anime, 1girl, batman",
            init_images=[image], 
            controlnet_input_image=[image], 
            controlnet_weight = 1,
            controlnet_guidance = 1,
            denoising_strength=0.7,
            sampler_index="Euler a",
            cfg_scale=7,
            controlnet_module='canny',
            controlnet_model='control_canny-fp16 [e3fe7712]',
           )
    return output.image

def saveimg(path, img):
    if not os.path.exists(path):
        os.makedirs(path)
    now = datetime.datetime.now()
    img.save(path+'/'+now.strftime('%Y%m%d%H%M%S%f')+'.png')

if __name__ == '__main__':
    pil_image = Image.open("D:\StudyLife\Github\HackIllinois\input/input2.png")
    image = controlNetImg2img(pil_image)
    saveimg("D:\StudyLife\Github\HackIllinois\output", image)
