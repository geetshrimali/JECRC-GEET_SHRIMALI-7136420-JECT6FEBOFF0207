import time

class TODO:
    todo = []
    
    def add_todo(self, desc):
        dict0 = {}
        dict0['id'] = int(time.time())
        dict0['desc'] = desc
        dict0['is_completed'] = False
        self.todo.append(dict0)
        return self.todo

    def remove_todo(self, id):
        for i in self.todo:
            if i['id'] == id:
                self.todo.remove(i)
                return 1
        else:
            return -1
                 
    
    def display_todos(self):
        return print(self.todo)
    
    def update_todo(self, id, new_desc):
        for i in self.todo:
            if i['id'] == id:
                i['desc'] = new_desc
    
    def toggle_mark_as_completed(self, id):
        for i in self.todo:
            if i['id'] == id:
                i['is_completed'] = True
    
    def completed_todos(self):
        for i in self.todo:
            if i['is_completed'] == True:
                print(i)
    
    def incompleted_todos(self):
        for i in self.todo:
            if i['is_completed'] == False:
                print(i)
