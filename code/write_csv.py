import os
import csv

BASE_PATH = os.path.dirname(os.path.abspath(__file__))+'/..'
file_path = '%s/data/test.csv' % BASE_PATH
file_path_del = '%s/data/test_del.csv' % BASE_PATH
lists = [['Gou', 26, 'Japan'], ['Suzuki', 26, 'Japan']]

#csvfileの作成
def write_csv(file_path):
    with open(file_path, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        writer.writerow(['Name', 'Age', 'Country'])
        writer.writerow(['Bob', 22, 'America'])
        writer.writerow(['Iku', 22, 'Japan'])
        writer.writerow(['Havra', 28, 'Mongoru'])

#csvfileに行を追加
def add_csv(file_path, lists):
    with open(file_path, 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        for line in lists:
            writer.writerow(line)

#csvfileの行を削除
def del_csv_by_age(file_path_r, file_path_w, age):
    csvfile_r = open(file_path_r, 'r', encoding='utf-8')
    csvfile_w = open(file_path_w, 'w', encoding='utf-8')
    reader = csv.DictReader(csvfile_r)
    writer = csv.writer(csvfile_w)
    c = 0
    for row in reader:
        c+=1
        if c == 1:
            writer.writerow(row.keys())
        if row['Age'] == age:
            continue
        writer.writerow(row.values())
    csvfile_w.close()
    csvfile_r.close()

#csvfileの読み込み
def read_csv(file_path):
    csvfile = open(file_path, 'r', encoding = 'utf-8')
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

#csvfileの辞書読み込み
def read_dict_csv(file_path):
    csvfile = open(file_path, 'r', encoding = 'utf-8')
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

if __name__ == '__main__':
    # write_csv(file_path)
    # add_csv(file_path, lists)
    del_csv_by_age(file_path, file_path_del, '22')
