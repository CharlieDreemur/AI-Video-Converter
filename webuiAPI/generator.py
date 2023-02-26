import webuiapi
import os
import datetime
from PIL import Image, PngImagePlugin
import json
import requests
import io
import base64
from io import BytesIO
from . import setting


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

#Convert image to base64
def pil_to_base64(pil_image):
    with BytesIO() as stream:
        pil_image.save(stream, "PNG", pnginfo=None)
        base64_str = str(base64.b64encode(stream.getvalue()), "utf-8")
        return "data:image/png;base64," + base64_str

        
def img2img(image, setup):
    #Convert image to base64
    url = setting.setup["url"]
    setup["init_images"] = [pil_to_base64(image)] #Plug converted Image to Payload
    response = requests.post(url=f'{url}/sdapi/v1/img2img', json=setup)
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

def controlNetImg2img(image, setup):
    cn = webuiapi.ControlNetInterface(api)
    output = cn.img2img(prompt= setup['prompt'],
            width=setup['width'],
            height=setup['height'],
            init_images=[image], 
            controlnet_input_image=[image], 
            steps= setup['steps'],
            controlnet_weight = setup['controlnet_weight'],
            controlnet_guidance = setup['controlnet_guidance'],
            denoising_strength= setup['denoising_strength'],
            sampler_index= setup['sampler_name'],
            cfg_scale= setup['cfg_scale'],
            controlnet_module= setup['controlnet_module'],
            controlnet_model= setup['controlnet_model'],
           )
    return output.image

def saveimg(img, path, fileName='output'):
    if not os.path.exists(path):
        os.makedirs(path)
    img.save(path + '/' + fileName + '.png', 'PNG')

if __name__ == '__main__':
    pil_image = Image.open('D:\StudyLife\Github\HackIllinois\input\young-woman-showing-smile-casual-260nw-601626770.webp')
    setting.setup_model_match(style="amime")
    setting.setup_type_match(type="character")
    image = controlNetImg2img(pil_image, setting.setup)
    saveimg(img = image, path="D:\StudyLife\Github\HackIllinois\output")
