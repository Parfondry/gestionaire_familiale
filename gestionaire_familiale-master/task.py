

class Task:

    def __init__(self, id, name,done=False):

        self.__id_task = id
        self.__name =name
        self.__done=done

    @property
    def name(self):
        return self.__name

    @property
    def done(self):
        return self.__done
    
    @property
    def id(self):
        return self.__id_task

    def set_done(self,new_done=True):
        self.__done=new_done
    
    def str(self):
        state=" est disponible !"
        if self.done:
            state=" a été effectuée !"
        print("la tache numéro "+ str(self.id) +" : "+self.name+ state)

    def add_task(self):

        newtask = input("Veuillez entrer votre nouvelle tâche (entre guillemets):")
        if not type(newtask) is str:
            raise TypeError("seulement str sont accepté")
    
        return newtask