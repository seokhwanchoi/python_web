from entity.models import Todo



def menu_display():
    print("======= 일정관리 시스템 =======")
    print("1. 전체 목록 보기 ")
    print("2. 등록 ")
    print("3. 수정 ")
    print("4. 삭제 ")
    print("5. 상세보기")
    print("0. 종료")


    
#menu select
def menu_select() :
    menu = input("메뉴를 선택하세요 : ")
    return menu

#message dispay
def message_display(message) :
    print(message)


#list display
def list_display(Todos) :
    print("=== 전체 목록 ===")
    for Todo in Todos :
        print(Todo.info())


#register todo
def input_display() :
    id = input("아이디 : ")
    title = input("이름 : ")
    contents = input("내용 : ")
    date = input("시작 날짜 : ")
    done = input("종료 날짜 : ")
    return Todo(id,title,contents, date,done)


#수정하거나 삭제 또는 상세보기위한 id 입력 화면
def id_input_display(command):
    id = input("{0} id는 ?  ".format(command))
    return id

#수정할 데이터 입력 화면
def update_input_display(id):
    title = input("이름 : ")
    contents = input("내용 : ")
    date = input("시작 날짜 : ")
    done = input("종료 날짜 : ")
    return Todo(id,title,contents, date,done)  

#person dispay
def todo_display(todo) :
    print("=== 상세 정보 ===")
    print(todo.info())
