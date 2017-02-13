# -*- coding:utf-8 -*-
""" 下载美国国家基础数据（hifld）
根据爬取的美国国家基础数据(hifld)种子下载数据

"""
import os
import json
from time import sleep

__author__ = 'cleland'


def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def download_dataset(speed_path, store_dir):
    create_dir(store_dir)
    with open(speed_path, 'r') as json_file:
        records = json.load(json_file)
    for record in records[:15]:
        category_name = record['category_name']
        dataset_name = record['dataset_name']
        dataset_url = record['dataset_url']
        category_dir = os.path.join(store_dir, category_name)
        create_dir(category_dir)
        dataset_path = os.path.join(category_dir, dataset_name) + '.csv'

        if not os.path.exists(dataset_path):
            os.system("wget {0} -O '{1}'".format(dataset_url, dataset_path))
        sleep(2)


def main():
    speed_path = '/Users/cleland/workspace/crawler/data/hifld_results.json'
    store_directory = '/Users/cleland/data/hifld'
    download_dataset(speed_path, store_directory)


if __name__ == '__main__':
    main()