#! -*- coding: utf-8 -*-
import jsonlines
import copy

BOOLQ_MODEL_OBJ = {
    "question": "",
    "title": "",
    "answer": "",
    "passage": ""
}

"""MultiNLIのデータ・フォーマットをBoolQのデータ・フォーマットに変換する"""


def main(path_multinli_jsonl: str,
         path_converted_jsonl: str):
    __boolq_objects = []
    writer = jsonlines.open(path_converted_jsonl, mode='w')
    with jsonlines.open(path_multinli_jsonl) as reader:
        for obj in reader:
            if obj['gold_label'] == 'neutral':
                label = ''
                continue
            elif obj['gold_label'] == 'entailment':
                label = 'Yes'
            elif obj['gold_label'] == 'contradiction':
                label = 'No'

            __boolq_obj = copy.deepcopy(BOOLQ_MODEL_OBJ)
            __boolq_obj['question'] = obj['sentence1']
            __boolq_obj['title'] = obj['pairID']
            __boolq_obj['answer'] = label
            __boolq_obj['passage'] = obj['sentence2']
            writer.write(__boolq_obj)

    writer.close()


def __main(__args):
    main(__args.path_multinli_jsonl, __args.path_converted_jsonl)


if __name__ == '__main__':
    import argparse
    opt = argparse.ArgumentParser()
    opt.add_argument('--path_multinli_jsonl', required=True)
    opt.add_argument('--path_converted_jsonl', required=True)
    args = opt.parse_args()
    __main(args)
