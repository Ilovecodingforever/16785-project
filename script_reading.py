from pylips.speech import RobotFace
from pylips.face import FacePresets




def read_from_ssh():
    import paramiko

    # SSH connection details
    hostname = "lop2.autonlab.org"
    username = "mingzhul"
    password = "<P$$Cu;{2xD$#l,qh(:3k+8`:"  # Consider using SSH keys for better security
    remote_file_path = "16785-project/script.txt"
    local_file_path = "local_file.txt"

    try:
        # Create an SSH client instance
        ssh_client = paramiko.SSHClient()

        # Automatically add the server's host key (less secure, for testing purposes only)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the SSH server
        ssh_client.connect(hostname=hostname, username=username, password=password)

        # Open an SFTP session
        sftp_client = ssh_client.open_sftp()

        # Download a file from the remote server
        sftp_client.get(remote_file_path, local_file_path)
        print(f"File downloaded successfully to {local_file_path}")

        # Upload a file to the remote server
        # sftp_client.put(local_file_path, remote_file_path)
        # print(f"File uploaded successfully to {remote_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the SFTP and SSH connections
        if sftp_client:
            sftp_client.close()
        if ssh_client:
            ssh_client.close()    




read_from_ssh()


# read the script
with open("script.txt", "r") as file:
    reply = file.read()


face = RobotFace()
face.say(reply)





pass

# generate_text()

# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]
# pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3")
# pipe(messages)

# from transformers import pipeline

# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]
# pipe = pipeline("text-generation", model="google-t5/t5-small")
# pipe(messages)


    # pipe = pipeline("text-generation", model="NousResearch/Hermes-3-Llama-3.2-3B")
    # pipe = pipeline("text-generation", model="SweatyCrayfish/llama-3-8b-quantized", device_map='auto')
    # model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
    # pipe = pipeline(
    #     "text-generation",
    #     model=model_id,
    #     model_kwargs={"torch_dtype": torch.bfloat16},
    #     device_map="auto",
    # )
    # pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3", device_map='auto')
    # pipe = pipeline("text-generation", model="MaziyarPanahi/Mistral-7B-Instruct-v0.3-GGUF")



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
