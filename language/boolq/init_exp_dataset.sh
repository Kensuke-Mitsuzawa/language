#!/usr/bin/env bash

mkdir datasets
mkdir datasets/boolean-questions
mkdir datasets/MultiNLI

wget -P datasets/boolean-questions https://storage.cloud.google.com/boolq/train.jsonl
wget -P datasets/boolean-questions https://storage.cloud.google.com/boolq/dev.jsonl

wget -P datasets/MultiNLI http://www.nyu.edu/projects/bowman/multinli/multinli_1.0.zip
wget -P datasets https://storage.googleapis.com/bert_models/2018_10_18/cased_L-12_H-768_A-12.zip
