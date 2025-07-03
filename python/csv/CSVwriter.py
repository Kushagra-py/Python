import csv
def accept():
    s_id=int(input('stu_id: '))
    sname=input('stu_name: ')
    game_n=input('game: ')
    results=input('result: ')
    headings=['sid','sname','game','res']
    data=[s_id,sname,game_n,results]
    f = open('results.csv', 'a', newline="")
    csvwriter=csv.writer(f)
    csvwriter.writerow(data)
    f.close
    repeat=input('continue?: ')
    while repeat != "n":
        accept()
accept()