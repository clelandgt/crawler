# -*- encoding:utf-8 -*-
""" 全球地震数据下载
下载1900~至今的全球2.5级以上地震数据
搜索页面： http://earthquake.usgs.gov/earthquakes/search/
"""
import os

__author__ = 'cleland'


def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def main():
    store_folder = '/Users/cleland//data/global_earthquake'
    create_dir(store_folder)
    import ipdb
    ipdb.set_trace()

    for year in xrange(2000, 2017):
        year_folder = os.path.join(store_folder, str(year))
        create_dir(year_folder)

        for month in xrange(1, 13):
            starttime = '{0}-{1}-1%2000:00:00'.format(year, month)
            if month == 12:
                endtime = '{0}-{1}-31%2023:59:59'.format(year, month)
            else:
                endtime = '{0}-{1}-1%2000:00:00'.format(year, month + 1)
            url = 'http://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime={0}&endtime={1}&minmagnitude=2.5&orderby=time'.format(starttime, endtime)
            file_path = os.path.join(year_folder, str(month)) + '.csv'
            os.system("wget {0} -O '{1}'".format(url, file_path))


if __name__ == '__main__':
    main()
