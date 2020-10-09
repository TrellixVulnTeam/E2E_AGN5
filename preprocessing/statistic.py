import json

DATASET_PATH = 'dataset'
MARKS_PATH = './preprocessing/marks.json'
E2E_RESULT_PATH = './E2E_Dataset.json'


def reverseDict(dict):
    return {v: k for k, v in dict.items()}


def getStats():
    stats = {}
    marks = json.load(open(MARKS_PATH))
    marks = reverseDict(marks)

    result = json.load(open(E2E_RESULT_PATH))
    for sentence in result.values():
        for c in sentence:
            if (c in marks):
                stats[marks[c]] = stats.get(marks[c], 0) + 0.5

    print(stats)
    return


if __name__ == "__main__":
    getStats()
    pass
