import re
import speech_recognition as sr
import time
import json
#import UnityEngine as ue



def talkToMe(audio):
    print(audio)
    for line in audio.splitlines():
        print("say " + line)

GOOGLE_CLOUD_SPEECH_CREDENTIALS = {
  "type": "service_account",
  "project_id": "skilful-ethos-347705",
  "private_key_id": "966b5b94fe9138ed2ec75b44f465dd2c8f2aab46",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCiO30O1t8XFDXa\nIPOhZ4BvwbFsg7QTPRIM/VDyUDADdI2PvdNY8XRiIh1mlAR67Gmkwoa7mSvBdB4c\nY2k10VE37Vs2YLaH/ICC3xRpxJasDbzPd1/wzRg8fCZ8CvlvGx8UTPpGnf9DnUyQ\nkxRiCES0CLvq3o3b5zbP1N7Utz40E1ivJW0AJvFS8DY/KH8FwEYc6cZSZaSLEmow\n/iVSdGBdckUgt+fMNR1w0olSu3JsmKZWGaEfzWQ7kPi5iT1S39z6BRe1gd8FZboX\nLWKnAN6K7LifBbWYyYnbR/P/gD7J649kPAYqiafcclDji33gzNR2pxooZBlg4HyX\nRzQLGblHAgMBAAECggEAG2NfoXm0//hxfvnBJ6aJkFRq158Eb5sHyRma6M2QzYSH\nwZSScZmRxF9uBztF5lqzGxWcGV+qe2ZXDwPZZzSHOaHgnDWHmz2NlIqEr7Z4mWNY\nVM4abFSzmsJ63MYdhhxWCt9UAUf7KDcODfpGnqY2sw4ma2hXGqDWKBAP7mlhHvlA\nRfcAvPWUtLjBjkiTKTmNuqgHLhkJwQkbZE6XRDwsnvRcXIYIk2dqsrE0fC+Z42GX\nep7Zeg7RYG6EFKPJSRgv3WryrQ6BPa8+/Twh0msMROJYRbFFD392u7TnuwisELh4\nKrMp4svufjUKaU2pfP2OaGi4nz/4aHTE+3Ouc1tgQQKBgQDVSYglzybU/H6ez8W9\nqkSyRnnaeLqJEVH5labWOKoEiwd0ZerUmvZf2nEEJPSeg2O5BFzVOzcatsPw/UDy\nC9mM508HGIzWco5BKLtrktLZfJk7Xu1wEuKRfftdDuUiplgLGX9+gCnAh92WijKw\neMyiy291GdOvWj1iDwrQ0appfQKBgQDCuI7es1pnQHmXRbAYgAY+xvC2NpYCQNu7\nolRDvnRD3vtONdcjQ2Kx4ISGKipGDTi/gDzLUQ066a9+f/D4+ltwVjWZlzEL/mBX\ngkWP0ukBimDh8lCqM8vM+f+xCoLhzHjXVKexLRvwuKQTyv/jL++kHFYpxxmVs2e+\nh6pLvQCJEwKBgQDSQeDDVQj04cx5Bl3q8VUzYaJyKp3IzZhAMLT9bXK9c8jviCEN\nYY4LRC4xZbT4JpJCK/jQA8X4wb87bI1/jwrxin0vg5YjOV7fASZxj5Xn7JqqGpR6\n7UMJJmaLgEmF9PHKT2KN9A40zDs3UhlSOmORAHdpuwIhVRY5+pYw8N/LiQKBgQC+\nkryZbzWiajLWf4jaYao7FJ+P5hqot+uWV0hbSPInXvvbzsvxIklcx91MJcZb6yLI\nIezeHERzjTSJ/RPNydFmP6mT2apSD7Mg0kncelI7hMBPQsX53lmvElpSXnQ8I899\nB8hbmkeHMF69VGdeZZMHrggSOV9r6Ts2+TYNjDwS6wKBgQCKF4IcFrvku7puvule\nZ4QPhG9BC0z5bW0o3L3tcN1Z02PBIq+iXMvM4YkbhEoGCayKeWOp2jUfqiX4BjCK\nAa/UkYQQDB+SX7lmiBUTo3ARaJpzY37h0LRL+fteTLq+3AM3ccPtAR792waivsFb\nxn3pbVjOsLtTpt1Mmi92Xf8EzA==\n-----END PRIVATE KEY-----\n",
  "client_email": "cs-534-final-project@skilful-ethos-347705.iam.gserviceaccount.com",
  "client_id": "106465958702647232396",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/cs-534-final-project%40skilful-ethos-347705.iam.gserviceaccount.com"
}


def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
        start_time = time.time()
        #command = r.recognize_google(audio).lower()
        #command = r.recognize_wit(audio, key="YGDX5CHECQDCZJOXMTEZK7VKFZKRV44I").lower()
        #command = r.recognize_azure(audio, key="49f6f6c541f244afb5b42d2648884232").lower() # requires modification to SR __init__.py
        #command = r.recognize_houndify(audio, client_id="oOyrgxTOCCk0qIHCUDjWXw==", client_key="BOUmRQg8lMm74vc2sejcxxwaxC1hQpaqt5jwzJD3Tf39Zhib7g7zd4idTcXLoeTqq4fqziI5LqiY3Mks8382UQ==").lower()
        #command = r.recognize_google_cloud(audio, credentials_json=json.dumps(GOOGLE_CLOUD_SPEECH_CREDENTIALS))
        elapsed_time = time.time() - start_time
        print('You said: ' + str(command))
        print("time: " + str(elapsed_time))

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command


def assistant(command):
    if re.search(r"quit|exit|close", command, re.IGNORECASE):
        return False
    else:
        talkToMe(f'You said {command}')
        return True

validCommands = ["blue", "red", "green"]   # can be changed to accept more words

if __name__ == "__main__":
    # while assistant(myCommand()):
    #    continue
    while True:
        command = myCommand()
        commands = command.split()
        #print(commands)
        for word in commands:
            if word in validCommands:
                print(word)
