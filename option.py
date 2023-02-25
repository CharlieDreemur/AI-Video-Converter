url = "http://127.0.0.1:7860"

# the fallback defaults for AIYA if bot host doesn't set anything
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


option_payload = {
    "sd_model_checkpoint": "Anything-V3.0-pruned.ckpt [2700c435]",
    "CLIP_stop_at_last_layers": 2
}


response = requests.post(url=f'{url}/sdapi/v1/options', json=option_payload)