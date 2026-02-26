import ollama

response = ollama.generate(
    model="llama3.1:8b",
    prompt="why are leaves of plant green in color?",
)

print(f"Response Object (TYPE) :\n {type(response)}")
print(f"Response Object (MODEL DUMPS TYPE):\n {type(response.model_dump())}")
print(f"Response Object (MODEL DUMPS):\n {response.model_dump()}")
print(f"Response Object (KEYS):\n {response.model_dump().keys()}")

'''
Response Object (TYPE) :
 <class 'ollama._types.GenerateResponse'>
Response Object (MODEL DUMPS TYPE):
 <class 'dict'>
Response Object (MODEL DUMPS):
{
    'model': 'llama3.1:8b',
    'created_at': '2026-02-26T07:14:57.843163Z',
    'done': True,
    'done_reason': 'stop',
    'total_duration': 59576652375,
    'load_duration': 4222267833,
    'prompt_eval_count': 19,
    'prompt_eval_duration': 7830841500,
    'eval_count': 402,
    'eval_duration': 47126110710,
    'response': "The reason why leaves of plants are generally green in color is due to the presence of a pigment called chlorophyll. Chlorophyll is a crucial molecule that plays a key role in photosynthesis, the process by which plants convert sunlight into energy.\n\nHere's what happens:\n\n1. **Chlorophyll absorbs light**: Chlorophyll molecules absorb light from the visible spectrum, especially blue and red light. This helps to trap energy from sunlight.\n2. **Conversion of light energy**: The absorbed light energy is then used to fuel a chemical reaction that converts carbon dioxide and water into glucose (sugar) and oxygen.\n\nNow, here's why chlorophyll makes leaves green:\n\n**Reflection and absorption**: Chlorophyll reflects blue light and absorbs red light, which means that it reflects the shorter wavelengths of visible light (like blue and violet) and absorbs longer wavelengths (like red and yellow). When we look at a leaf, our eyes see the reflected light, which is primarily in the green spectrum.\n\n**Other pigments**: While chlorophyll is the dominant pigment responsible for photosynthesis, other pigments like carotenoids and anthocyanins can also be present in leaves. Carotenoids are responsible for yellow, orange, and red colors, while anthocyanins produce red and purple hues. However, these pigments are usually masked by the green color of chlorophyll.\n\n**Why is green the optimal color?**: Green light has a wavelength that's easily absorbed by chlorophyll, making it an ideal choice for photosynthesis. The green color also helps to:\n\n* **Reduce photorespiration**: Excess energy from sunlight can lead to photorespiration, which can be detrimental to plant growth.\n* **Increase efficiency**: Chlorophyll's absorption spectrum allows plants to capture light most efficiently.\n\nIn summary, the green color of leaves is a result of chlorophyll's ability to absorb and reflect light in specific ways, making it an essential component for photosynthesis.",
    'thinking': None,
    'context': [128006, 882, 128007, 271, 35734, 527, 11141, 315, 6136, 6307, 304, 1933, 30, 128009, 128006, 78191, 128007, 271, 791, 2944, 3249, 11141, 315, 11012, 527, 8965, 6307, 304, 1933, 374, 4245, 311, 279, 9546, 315, 264, 77678, 2663, 37833, 5237, 25734, 13, 92479, 5237, 25734, 374, 264, 16996, 43030, 430, 11335, 264, 1401, 3560, 304, 7397, 74767, 11, 279, 1920, 555, 902, 11012, 5625, 40120, 1139, 4907, 382, 8586, 596, 1148, 8741, 1473, 16, 13, 3146, 1163, 9761, 5237, 25734, 91111, 3177, 96618, 92479, 5237, 25734, 35715, 35406, 3177, 505, 279, 9621, 20326, 11, 5423, 6437, 323, 2579, 3177, 13, 1115, 8779, 311, 23709, 4907, 505, 40120, 627, 17, 13, 3146, 49337, 315, 3177, 4907, 96618, 578, 42101, 3177, 4907, 374, 1243, 1511, 311, 10633, 264, 11742, 13010, 430, 33822, 12782, 40589, 323, 3090, 1139, 34323, 320, 82, 8734, 8, 323, 24463, 382, 7184, 11, 1618, 596, 3249, 37833, 5237, 25734, 3727, 11141, 6307, 1473, 334, 45338, 323, 44225, 96618, 92479, 5237, 25734, 27053, 6437, 3177, 323, 91111, 2579, 3177, 11, 902, 3445, 430, 433, 27053, 279, 24210, 93959, 315, 9621, 3177, 320, 4908, 6437, 323, 80836, 8, 323, 91111, 5129, 93959, 320, 4908, 2579, 323, 14071, 570, 3277, 584, 1427, 520, 264, 16312, 11, 1057, 6548, 1518, 279, 27000, 3177, 11, 902, 374, 15871, 304, 279, 6307, 20326, 382, 334, 11663, 24623, 1392, 96618, 6104, 37833, 5237, 25734, 374, 279, 25462, 77678, 8647, 369, 7397, 74767, 11, 1023, 24623, 1392, 1093, 1841, 66728, 17390, 323, 23064, 511, 8503, 1354, 649, 1101, 387, 3118, 304, 11141, 13, 3341, 66728, 17390, 527, 8647, 369, 14071, 11, 19087, 11, 323, 2579, 8146, 11, 1418, 23064, 511, 8503, 1354, 8356, 2579, 323, 25977, 82757, 13, 4452, 11, 1521, 24623, 1392, 527, 6118, 43248, 555, 279, 6307, 1933, 315, 37833, 5237, 25734, 382, 334, 10445, 374, 6307, 279, 23669, 1933, 30, 96618, 7997, 3177, 706, 264, 46406, 430, 596, 6847, 42101, 555, 37833, 5237, 25734, 11, 3339, 433, 459, 10728, 5873, 369, 7397, 74767, 13, 578, 6307, 1933, 1101, 8779, 311, 1473, 9, 3146, 51425, 6685, 417, 29579, 96618, 1398, 1140, 4907, 505, 40120, 649, 3063, 311, 6685, 417, 29579, 11, 902, 649, 387, 65069, 311, 6136, 6650, 627, 9, 3146, 70656, 15374, 96618, 92479, 5237, 25734, 596, 44225, 20326, 6276, 11012, 311, 12602, 3177, 1455, 30820, 382, 644, 12399, 11, 279, 6307, 1933, 315, 11141, 374, 264, 1121, 315, 37833, 5237, 25734, 596, 5845, 311, 35406, 323, 8881, 3177, 304, 3230, 5627, 11, 3339, 433, 459, 7718, 3777, 369, 7397, 74767, 13],
    'logprobs': None
}
Response Object (KEYS):
dict_keys([
    'model',
    'created_at',
    'done',
    'done_reason',
    'total_duration',
    'load_duration',
    'prompt_eval_count',
    'prompt_eval_duration',
    'eval_count',
    'eval_duration',
    'response',
    'thinking',
    'context',
    'logprobs'
])
'''