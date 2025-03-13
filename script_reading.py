from pylips.speech import RobotFace
from pylips.face import FacePresets


# import torch
# from transformers import AutoModel, AutoModelForCausalLM
# from optimum.bettertransformer import BetterTransformer
# model = AutoModelForCausalLM.from_pretrained("gpt2-large", torch_dtype=torch.float16)
# # model = BetterTransformer.transform(model)


# from transformers import AutoTokenizer
# tokenizer = AutoTokenizer.from_pretrained("gpt2-large")
# pt_batch = tokenizer(
#     ["We are very happy to show you the 🤗 Transformers library.", "We hope you don't hate it."],
#     padding=True,
#     truncation=True,
#     max_length=512,
#     return_tensors="pt",
# )



# from transformers import T5Tokenizer, T5ForConditionalGeneration

# tokenizer = T5Tokenizer.from_pretrained("google-t5/t5-small")
# model = T5ForConditionalGeneration.from_pretrained("google-t5/t5-small")

# input_ids = tokenizer("respond to this: how are you", return_tensors="pt").input_ids
# outputs = model.generate(input_ids)
# print(tokenizer.decode(outputs[0], skip_special_tokens=True))


from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="NousResearch/Hermes-3-Llama-3.2-3B")
print(messages)
print(pipe(messages))


messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3")
pipe(messages)

from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="google-t5/t5-small")     
pipe(messages)


# read the script
with open("script.txt", "r") as file:
    script = file.read()


face = RobotFace()
face.say(script)




pass

# actors = {
#         'FARQUAAD': RobotFace(robot_name='FARQUAAD', voice_id="com.apple.voice.compact.en-GB.Daniel"),
#     }

# actors['FARQUAAD'].set_appearance(FacePresets.chili)

# for line in script.split('\n'):
#     if ':' not in line:
#         continue

#     actor, content = line.split(':')
#     face = actors[actor]
#     face.say(content)
#     face.wait()