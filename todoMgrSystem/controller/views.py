
from exception.exceptions import DuplicateError, NotFoundError
from dao.file_registry import save_file, init_data_load  

class TodoController:
    todos = [] #클래스 변수


    def register(self,todo) :
    #id 중복 check  - 중복될 경우 DuplicateError(id)
        index = self.is_exist(todo.id) 
        if index > -1 :
            raise DuplicateError(todo.id) 
        TodoController.todos.append(todo)

    def update(self,todo):
        #id check  - 존재하지 않는 경우 NotFoundError(id)
        index = self.is_exist(todo.id)
        if index == -1 :
            raise NotFoundError(todo.id)
        TodoController.todos[index] = todo

    def remove(self,id):
        #id check  - 존재하지 않는 경우 NotFoundError(id)
        index = self.is_exist(id)
        if index == -1 :
            raise NotFoundError(id)
        TodoController.todos.pop(index)

    def getTodo(self,id) :
        #id check  - 존재하지 않는 경우 NotFoundError(id)
        index = self.is_exist(id)
        if index == -1 :
            raise NotFoundError(id)
        return TodoController.todos[index]

    def getAllTodos(self) :
        return TodoController.todos

    def is_exist(self,id) :
        for index, todo in enumerate(TodoController.todos) :
            if todo.id == id :
                return index
        return -1

    def save_list(self):
        save_file(TodoController.todos)

    def load_list(self):
       
        TodoController.todos = init_data_load()
        print("load_list : ",TodoController.todos)