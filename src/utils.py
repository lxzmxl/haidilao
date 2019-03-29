import pandas as pd



def read_txt(txt):
    """
    read the text file
    """
    with open(txt, 'r') as f:
        raw_total_list = f.readline()
        # total_list = []
        if 'cross.txt' in txt:
            column = ['id', 'roadID1', 'roadID2', 'roadID3', 'roadID4']
        else:
            column = raw_total_list.strip('#').strip('\n').strip('(').strip(')').split(',')

        df = pd.DataFrame(columns=column)
        for line in f:
            each_list = line.strip('\n').strip('(').strip(')').split(',')
            each_list = [int(i) for i in each_list]
            df.loc[len(df.index)] = each_list
            # total_list.append(each_list)

    return df


if __name__ == '__main__':
    read_txt('./SDK/SDK_python/CodeCraft-2019/config/car.txt')
