#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ Command interpreter for AirBnB """
    
    prompt = '(hbnb) '
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program on EOF"""
        return True

    def do_help(self, line):
        """Display help information"""
        if not line:
            cmd.Cmd.do_help(self, line)
        else:
            try:
                func = getattr(self, 'help_' + line)
                func()
            except AttributeError:
                print(f"No help on '{line}'")

    def emptyline(self):
        """Override emptyline to prevent execution of empty lines"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if not line:
            print("** class name missing **")
            return
        
        class_name = line
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        print(obj.id)
    
    def do_show(self, line):
        """Prints the string representation of
        an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        obj = storage.all().pop(key, None)
        if obj is None:
            print("** no instance found **")
        else:
            storage.save()
    
    def do_all(self, line):
        """Prints all string representation of
        all instances based or not on the class name"""
        args = line.split()
        if args and args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        
        if args:
            class_name = args[0]
            objs = [str(obj) for key, obj in storage.all().items() if key.startswith(class_name)]
        else:
            objs = [str(obj) for obj in storage.all().values()]
        
        print(objs)
    
    def do_update(self, line):
        """Updates an instance based on the
        class name and id by adding or updating attribute"""
        args = line.split()
        if len(args) < 3:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        
        if len(args) < 4:
            print("** instance id missing **")
            return
        
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        
        if len(args) < 5:
            print("** attribute name missing **")
            return
        
        attr_name = args[2]
        if len(args) < 6:
            print("** value missing **")
            return
        
        attr_value = args[3]
        if attr_name in ["id", "created_at", "updated_at"]:
            print("** cannot update attribute **")
            return
        
        setattr(obj, attr_name, attr_value)
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
