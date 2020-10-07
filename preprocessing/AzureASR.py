from azure.core.credentials import AzureKeyCredential
import azure.cognitiveservices.speech as speechsdk

import json


class AzureASR():
    def __init__(self):
        azure_asr_keys = json.load(open('./keys/Azure-ASR-keys.json'))
        speech_key, service_region = azure_asr_keys['key1'], azure_asr_keys['location']
        self.speech_config = speechsdk.SpeechConfig(
            subscription=speech_key, region=service_region)
        return

    def recognize(self, file_path):
        audio_input = speechsdk.AudioConfig(filename=file_path)
        speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config, audio_config=audio_input)

        result = speech_recognizer.recognize_once()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text

        if result.reason == speechsdk.ResultReason.NoMatch:
            raise Exception("No speech could be recognized: {}".format(
                result.no_match_details))

        if result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            raise Exception("Speech Recognition canceled: {}".format(
                cancellation_details.reason))

            # if cancellation_details.reason == speechsdk.CancellationReason.Error:
            #     print("Error details: {}".format(cancellation_details.error_details))

        return
