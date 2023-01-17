import openai
import requests
import json
from enum import Enum

openai.api_key = ""
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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'
}
openaiCompletionUrl = " https://api.openai.com/v1/completions"

openaiImageUrl = " https://api.openai.com/v1/images/generations"


class Product(Enum):
    RING = 'ring'
    NECKLACE = 'necklace'
    PENDANT = 'pendant'
    BRACELET = 'bracelet'


ACCEPTED_PRODUCTS = [i.value for i in Product]


class Material(Enum):
    GOLD = 'gold'
    DIAMOND = 'diamond'
    SILVER = 'silver'
    PRECIOUSSTONES = 'precious stones'


ACCEPTED_MATERIALS = [i.value for i in Material]


class Gender(Enum):
    FEMALE = 'female'
    MALE = 'male'


class Style(Enum):
    CLASSIC = 'classic'
    TRENDY = 'trendy'
    FUTURISTIC = 'futuristic'


ACCEPTED_STYLE = [i.value for i in Style]


def generate_prompt(product, material, gender, style, custom_names=None):
    if len(material) == 1:
        material = material[0]
    else:
        material = ", ".join(x for x in material)
    prompt = f"Write a prompt for DALL-E to generate a {material} {product}, "
    if custom_names:
        prompt += f"with custom names: {custom_names}, "
    prompt += f"designed for {gender} and style it as {style}.Give DALL-E details as if you are a jewelery designer. " \
              f"Make it as if you are sending it to the jewels industry."

    data = {"model": "text-davinci-003", "prompt": prompt, "temperature": 0.8, "max_tokens": 1000}
    res = requests.post(openaiCompletionUrl, json.dumps(data), headers=headers)
    result = res.json()
    result = result['choices'][0]['text']

    print(result)
    return prompt, result


def generate_image(prompt):
    data = {'prompt': prompt, 'n': 4, 'size': '1024x1024'}
    res = requests.post(openaiImageUrl, json.dumps(data), headers=headers)
    result = res.json()
    print(result)
    return result


def generate_jewelery(form_data):
    product = form_data['product']
    if product not in ACCEPTED_PRODUCTS:
        return False, f'Product {product} is not accepted. Accepted products are: {ACCEPTED_PRODUCTS}'

    material = form_data.getlist('material')
    for m in material:
        if m not in ACCEPTED_MATERIALS:
            return False, f'Material {m} is not accepted. Accepted materials are: {ACCEPTED_STYLE}'
    gender = form_data.get('gender')
    if gender not in ['female', 'male']:
        return False, f'Gender {gender} is undefined. Choose Female or Male.'
    style = form_data.get('style')
    if style not in ACCEPTED_STYLE:
        return False, f'Style {style} is not accepted. Accepted styles are {ACCEPTED_STYLE}'

    custom_names = form_data.get('names', None)
    print(f'custom names: {custom_names}')
    prompt_sent, prompt_generated = generate_prompt(product, material, gender, style, custom_names)
    images = generate_image(prompt_generated)
    images['prompt_sent'] = prompt_sent
    images['prompt_generated'] = prompt_generated
    return True, images
