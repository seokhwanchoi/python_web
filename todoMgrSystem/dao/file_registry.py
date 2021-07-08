
from entity.models import Todo
import os


def save_file(todos) :
    #프로그램 종료시 views.py todos list를 파일저장
    save_file = open("list.dat", "w")

    for index, t in enumerate(todos) :
        if isinstance(t, Todo) :
            save_file.write("{0},{1},{2},{3},{4}\n".format(t.id,t.title,t.contents, t.date, t.done))
       
    save_file.close()

def init_data_load() :
    #프로그램 시작시 파일읽어서 views.py todos list에 저장
    todos=[]
    fileExist = os.path.isfile("list.dat")
    if fileExist:
        read_file=open("list.dat","r")
        while True:
            
            data = read_file.readline()
            if not data : break
            data_list=data.split(",")

            todo =Todo(data_list[0],data_list[1],data_list[2],data_list[3],data_list[4].strip("\n"))
            todos.append(todo)

            
        read_file.close()

    return todos