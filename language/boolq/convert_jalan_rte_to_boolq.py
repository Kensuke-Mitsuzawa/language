#! -*- coding: utf-8 -*-
import jsonlines
import copy
import csv

BOOLQ_MODEL_OBJ = {
    "question": "",
    "title": "",
    "answer": "",
    "passage": ""
}

"""Jalanのデータ・フォーマットをBoolQのデータ・フォーマットに変換する"""


def main(path_jalan_tsv: str,
         path_converted_jsonl: str):
    __boolq_objects = []
    writer = jsonlines.open(path_converted_jsonl, mode='w')
    with open(path_jalan_tsv) as reader:
        read = csv.reader(reader, dialect='excel-tab')
        for obj in read:
            if obj[1] == '1':
                label = 'Yes'
            elif obj[1] == '0':
                label = 'No'
            else:
                raise Exception(f'Label {obj[1]} is not defined.')

            __boolq_obj = copy.deepcopy(BOOLQ_MODEL_OBJ)
            __boolq_obj['question'] = obj[2]
            __boolq_obj['title'] = obj[0]
            __boolq_obj['answer'] = label
            __boolq_obj['passage'] = obj[3]
            writer.write(__boolq_obj)

    writer.close()


def __main(__args):
    main(__args.path_jalan_tsv, __args.path_converted_jsonl)


if __name__ == '__main__':
    import argparse
    opt = argparse.ArgumentParser()
    opt.add_argument('--path_jalan_tsv', required=True)
    opt.add_argument('--path_converted_jsonl', required=True)
    args = opt.parse_args()
    __main(args)
