import requests


# the defaults if doesn't set anything
setup = {
    "url": "http://127.0.0.1:7860",
    "sd_model_checkpoint": "anything-v4.5-pruned",
    "fps": 30,
    "prompt": "best quality, 8K, highres, masterpiece, anime, 1girl, cute, highly detailed",
    "negative_prompt": "(worst quality), (bad quality), nsfw, easynative",
    #Sampling
    "sampling_index": "Euler a",
    "steps": 40,
    "denoising_strength": 0.5,
    "seed": 114514,
    "cfg_scale": 12,
    #image
    "width": 512,
    "height": 512,
    "restore_faces": False,
    #controlNet
    "controlnet_module":'canny',
    "controlnet_model":'control_canny-fp16 [e3fe7712]',
    "controlnet_weight": 1,
    "controlnet_guidance": 1,
    
}
def setup_model_match(style):
    if style == "anime":
        setup["sd_model_checkpoint"] = "anything-v4.5-pruned"
    if style == "realistic":
        setup["sd_model_checkpoint"] = "dreamlike-photoreal-2.0"
        setup["prompt"] += "(photo-realistic),"
    if style == "3D-anime":
        setup["sd_model_checkpoint"] = "protogenV22Anime_22"
    if style == "art":
        setup["sd_model_checkpoint"] = "dreamlikeDiffusion10_10"
        setup["prompt"] += "dreamlikeart,"
    set_option(setup)
    
def setup_type_match(type):
    if type == "general":
        setup["controlnet_module"] = 'hed'
        setup["controlnet_model"] = 'control_hed-fp16 [13fee50b]'
    if type == "character":
        setup["controlnet_module"] = 'canny'
        setup["controlnet_model"] = 'control_canny-fp16 [e3fe7712]'
    if type == "building":
        setup["controlnet_module"] = 'mlsd'
        setup["controlnet_model"] = 'control_mlsd-fp16 [e3705cfa]'
    if type == "dance":
        setup["controlnet_module"] = 'openpose'
        setup["controlnet_model"] = 'control_openpose-fp16 [9ca67cc5]'
    set_option(setup)

def add_prompt(prompt):
    setup["prompt"] += prompt

def get_models_name():
    url = setup["url"]
    response = requests.get(url=f'{url}/sdapi/v1/sd-models')
    if response.status_code == 200:  # 200 indicates success
        data = response.json()  # Parse the response as JSON
        models_name=[]
        for(i, model) in enumerate(data):
            models_name.append(model["model_name"])
        return models_name
    else:
        print(f'Request failed with status code {response.status_code}')



def set_option(setup):
    option_payload = {
        "sd_model_checkpoint": setup["sd_model_checkpoint"],
        #"CLIP_stop_at_last_layers": 2
    }
    url = setup["url"]
    response = requests.post(url=f'{url}/sdapi/v1/options', json=option_payload)
    if response.status_code == 200:
        print("Set option successfully to "+sd_model_checkpoint)
    else:
        print(f'Request failed with status code {response.status_code}')

if __name__ == '__main__':
    print(get_models_name())
    set_option('dreamlike-photoreal-2.0')
