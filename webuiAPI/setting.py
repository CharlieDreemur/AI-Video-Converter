import requests
url = "http://127.0.0.1:7860"

# the defaults if doesn't set anything
template = {
    "negative_prompt": "",
    "data_model": "",
    "steps": 30,
    "max_steps": 50,
    "width": 512,
    "height": 512,
    "guidance_scale": "7.0",
    "sampler": "Euler a",
    "style": "None",
    "facefix": "None",
    "highres_fix": 'Disabled',
    "clip_skip": 1,
    "hypernet": "None",
    "lora": "None",
    "strength": "0.75",
    "batch": "1,1",
    "max_batch": "1,1",
    "upscaler_1": "ESRGAN_4x"
}

def get_models_name():
    response = requests.get(url=f'{url}/sdapi/v1/sd-models')
    if response.status_code == 200:  # 200 indicates success
        data = response.json()  # Parse the response as JSON
        for(i, model) in enumerate(data):
            models_name=[]
            models_name.append(model["model_name"])
            return models_name
    else:
        print(f'Request failed with status code {response.status_code}')

def get_sampler_name():
    response = requests.get(url=f'{url}/sdapi/v1/sampler')
    if response.status_code == 200:  # 200 indicates success
        data = response.json()  # Parse the response as JSON
        for(i, model) in enumerate(data):
            sampler_name=[]
            sampler_name.append(model["model_name"])
            return sampler_name
    else:
        print(f'Request failed with status code {response.status_code}')


def set_option(setup):
    option_payload = {
        "sd_model_checkpoint": "Anything-V3.0-pruned.ckpt [2700c435]",
        #"CLIP_stop_at_last_layers": 2
    }
    response = requests.post(url=f'{url}/sdapi/v1/options', json=option_payload)
    
if __name__ == '__main__':
    get_models_name()
    get_sampler_name()
