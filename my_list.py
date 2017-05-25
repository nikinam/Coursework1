
class Abstract_list:
    def add(self, el):
        raise NotImplementedError('add must be define')

    def remove(self,el):
        raise NotImplementedError('remove must be define')

    def to_string(self):
        raise NotImplementedError('to_string must be define')

class Mylist(Abstract_list):
    list = []
    def add (self , el):
        self.list.append(el)
    def remove(self,el):
        self.list.remove(el)

    def to_string(self):
        return self.list

m = Mylist()
m.to_string()

