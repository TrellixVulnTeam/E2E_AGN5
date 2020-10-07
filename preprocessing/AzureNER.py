
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

import json


class AzureNER():
    def __init__(self):
        azure_ner_keys = json.load(open('./keys/Azure-NER-keys.json'))
        key = azure_ner_keys['key1']
        endpoint = azure_ner_keys['endpoint']

        ta_credential = AzureKeyCredential(key)
        self.client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=ta_credential)

        return

    def entity_recognition(self, documents):
        if (documents == None or len(documents) < 1):
            raise Exception("Document is null")

        result = self.client.recognize_entities(documents=documents)

        # print("Named Entities:\n")
        # for entity in result.entities:
        #     print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
        #           "\n\tConfidence Score: \t", round(entity.confidence_score, 2), "\tLength: \t", entity.length, "\tOffset: \t", entity.offset, "\n")

        return result
