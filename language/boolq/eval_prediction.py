#! -*- coding: utf-8 -*-

import csv
from typing import Tuple
from collections import Counter


def return_evaluation_type(prediction_label: str,
                           gold_label: str,
                           label_predictions: Tuple[str, str] = ('True', 'False'),
                           label_golds: Tuple[str, str] = ('Yes', 'No')
                           ) -> str:
    index_prediction = label_predictions.index(prediction_label)
    index_gold = label_golds.index(gold_label)
    if index_prediction == 0 and index_gold == 0:
        return 'tp'
    elif index_prediction == 1 and index_gold == 0:
        return 'fn'
    elif index_prediction == 0 and index_gold == 1:
        return 'fp'
    elif index_prediction == 1 and index_gold == 1:
        return 'tn'
    else:
        raise Exception()


def main(path_prediction_csv: str,
         label_predictions: Tuple[str, str] = ('True', 'False'),
         label_golds: Tuple[str, str] = ('Yes', 'No')):
    csvfile = open(path_prediction_csv)
    reader_obj = csv.reader(csvfile)
    next(reader_obj)
    __stack = []
    for row in reader_obj:
        evaluation_type = return_evaluation_type(row[1], row[2], label_predictions, label_golds)
        __stack.append(evaluation_type)
    csvfile.close()

    dict_evaluation_sum = dict(Counter(__stack))
    precision = dict_evaluation_sum['tp'] / (dict_evaluation_sum['tp'] + dict_evaluation_sum['fp'])
    recall = dict_evaluation_sum['tp'] / (dict_evaluation_sum['tp'] + dict_evaluation_sum['fn'])
    f = (2 * precision * recall) / (precision + recall)

    print(f"tp: {dict_evaluation_sum['tp']}, fp: {dict_evaluation_sum['fp']}, fn: {dict_evaluation_sum['fn']}, tn: {dict_evaluation_sum['tn']}")
    print(f'precision: {precision} = {dict_evaluation_sum["tp"]} / ({dict_evaluation_sum["tp"]} + {dict_evaluation_sum["fp"]})')
    print(f'recall: {recall} = {dict_evaluation_sum["tp"]} / ({dict_evaluation_sum["tp"]} + {dict_evaluation_sum["fn"]})')
    print(f'f: {f} = (2 * {precision} * {recall}) / ({precision} + {recall})')


def __main(__args):
    __label_prediction = __args.label_prediction
    __label_gold = __args.label_gold
    main(__args.path_prediction_csv,
         __label_prediction,
         __label_gold)


if __name__ == '__main__':
    import argparse
    opt = argparse.ArgumentParser()
    opt.add_argument('--path_prediction_csv', required=True)
    opt.add_argument('--label_prediction', required=False, nargs='+', default=['True', 'False'])
    opt.add_argument('--label_gold', required=False, nargs='+', default=['Yes', 'No'])
    args = opt.parse_args()
    __main(args)

