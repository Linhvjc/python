from aspeak import SpeechToSpeakerService, ResultReason
import time

def say(text = "Nothing to say"):
    # try:
    #     speech = SpeechToSpeakerService()
    #     result = speech.text_to_speech(text,voice="en-US-JennyNeural", rate="+0%", pitch="+30%", style="cheerful")
    #     if result.reason != ResultReason.SynthesizingAudioCompleted:
    #         print("Failed to synthesize speech.")
    # except:
    #     print("Error occurred while synthesizing speech.")
    start = time.time()
    speech = SpeechToSpeakerService()
    end = time.time()
    print("Average1: " +str(end - start))
    start = time.time()
    speech.text_to_speech(text,voice="en-US-JennyNeural", rate="+0%", pitch="+30%", style="cheerful")
    end = time.time()
    print("Average2: " +str(end - start))
    # if result.reason != ResultReason.SynthesizingAudioCompleted:
    #     print("Failed to synthesize speech.")

if __name__ == "__main__":
    say("Hello what can I do")
