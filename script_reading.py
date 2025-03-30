from pylips.speech import RobotFace
from pylips.face import FacePresets
from pylips.face import ExpressionPresets


# read the script
with open("script.txt", "r") as file:
    reply = file.readlines()


emotion = reply[-1]
reply = ",".join(reply[0: -1])

face = RobotFace()
if 'happy' in emotion:
    face.express(ExpressionPresets.happy, 1000)
elif 'sad' in emotion:
    face.express(ExpressionPresets.sad, 1000)
elif 'surprise' in emotion:
    face.express(ExpressionPresets.surprise, 1000)
elif 'fear' in emotion:
    face.express(ExpressionPresets.fear, 1000)
elif 'angry' in emotion:
    face.express(ExpressionPresets.angry, 1000)
elif 'disgust' in emotion:
    face.express(ExpressionPresets.disgust, 1000)
else:
    face.express(ExpressionPresets.default, 1000)


face.say(reply)
face.wait()
