
from exception.exceptions import DuplicateError, NotFoundError
from entity.models import Todo
from view.templates import todo_display,input_display, list_display, menu_display, menu_select, message_display, id_input_display, update_input_display
from controller.views import TodoController

tc=TodoController()
tc.load_list()


while True :
    menu_display()
    menu = menu_select()
    if menu == "1" :
    #목록보기 views getAllTodos() 인사목록 리턴받아서 templates의 list_display()
        todoList = tc.getAllTodos()
        print(todoList)
        list_display(todoList)

    elif menu == "2" : 
 
    # DuplicateError 처리
        while True :  
            todo = input_display()
            try :
                tc.register(todo)
                message_display(todo.id+" 등록성공")
            except DuplicateError as error :
                message_display(error)
            
            break

            
    elif menu == "3" :
        id = id_input_display("수정")
        try: 
            todo = tc.getTodo(id)


            new_todo = update_input_display(id)
            tc.update(new_todo)
            message_display(id+" 수정성공")
        except NotFoundError as error :  # NotFoundError 처리
            message_display(error)
        
    elif menu == "4" :
    #삭제 - 삭제할 id 입력받고 views의 remove(id) 호출
        id = id_input_display("삭제")
        try :
            tc.remove(id)
            message_display(id+" 삭제성공")
        except NotFoundError as error : # NotFoundError 처리  
            message_display(error)
            
    elif menu == "5" : 
    #상세보기 - 상세보기할 id 입력받고 views의 getTodo(id) 호출
        id = id_input_display("검색")
        try:
            todo= tc.getTodo(id)
            todo_display(todo)       
        except NotFoundError as error:
            message_display(error)        
            
    elif menu =="0" :
        tc.save_list()
        message_display("일정관리시스템을 종료합니다.")
        break
    else :
        print()
        message_display("1,2,3,4,5,0 번 중 선택하세요") 