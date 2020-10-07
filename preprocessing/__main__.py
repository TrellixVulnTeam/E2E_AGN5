import os
from AzureNER import AzureNER
from AzureASR import AzureASR

import json

DATASET_PATH = 'dataset'
MARKS_PATH = './preprocessing/marks.json'
E2E_RESULT_PATH = './E2E_Dataset.json'


def preprocessing():
    azureASR = AzureASR()
    azureNER = AzureNER()

    marks = json.load(open(MARKS_PATH))

    result = {}
    if (os.path.isfile(E2E_RESULT_PATH)):
        result = json.load(open(E2E_RESULT_PATH))

    # count = round(len(os.listdir(DATASET_PATH)) * 0.7)
    count = 5

    for fileName in os.listdir(DATASET_PATH):
        if (count == 0):
            break

        full_path = os.path.join(DATASET_PATH, fileName)

        if (fileName not in result):
            result[fileName] = azureASR.recognize(full_path)

        count -= 1

    ner_results = azureNER.entity_recognition(list(result.values()))

    for fileName in result:
        ner_result = ner_results.pop(0)
        for entity in ner_result.entities:
            mark = marks[entity.category]
            result[fileName] = result[fileName].replace(
                entity.text, mark + entity.text + mark)

    json.dump(result, open(E2E_RESULT_PATH, 'w'))


if __name__ == "__main__":
    try:
        preprocessing()
    except Exception as ex:
        print(ex)
