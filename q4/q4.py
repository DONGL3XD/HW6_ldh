import matplotlib.pyplot as p
import csv

def main():
    f = open('202303subway.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')
    header = next(data)

    in_list = []
    out_list = []
    inout_list = []

    in_max30_val = []
    out_max30_val = []
    inout_max30_val = []

    in_max30_stname = []
    out_max30_stname = []
    inout_max30_stname = []
    
    for row in data:
        row = list(map(lambda s : ''.join(s.split()), row))
        
        in_psg = int(row[9]) + int(row[11])
        out_psg = int(row[10]) + int(row[12])
        inout_psg = in_psg + out_psg

        in_psg_li = [row[1] + '/' +row[2], in_psg]
        out_psg_li = [row[1] + '/' +row[2], out_psg]
        inout_psg_li = [row[1] + '/' +row[2], inout_psg]
        
        in_list.append(in_psg_li)
        out_list.append(out_psg_li)
        inout_list.append(inout_psg_li)
        
    in_list.sort(key=lambda x:-x[1])
    out_list.sort(key=lambda x:-x[1])
    inout_list.sort(key=lambda x:-x[1])

    for i in range(30):
        in_max30_val.append(in_list[i][1])
        out_max30_val.append(out_list[i][1])
        inout_max30_val.append(inout_list[i][1])

        in_max30_stname.append(in_list[i][0])
        out_max30_stname.append(out_list[i][0])
        inout_max30_stname.append(inout_list[i][0])
        
    f.close()    

    p.rc('font', family='Malgun Gothic', size=7)
    p.rcParams['axes.unicode_minus'] = False
    

    p.subplot(1, 3, 1)
    p.bar(in_max30_stname, in_max30_val, color='r')
    p.title("승차 승객 순위")
    p.xticks(rotation=90)

    p.subplot(1, 3, 2)
    p.bar(out_max30_stname, out_max30_val, color='g')
    p.title("하차 승객 순위")
    p.xticks(rotation=90)

    p.subplot(1, 3, 3)
    p.bar(inout_max30_stname, inout_max30_val, color='b')
    p.title("승하차 승객 순위")
    p.xticks(rotation=90)


    p.subplots_adjust(left=0.05, bottom=0.2, right=0.95, top=0.9, wspace=0.2, hspace=0.2)
    
    p.show()

main()
