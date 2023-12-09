#!/usr/bin/python3
"""console that cointain the entry poin of interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF end of file then exit"""
        print()
        return True

    def emptyline(self):
        """do nothing when empty line pass"""
        pass

    def do_create(self, line):
        """creating a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return
        try:
            lines = line.split()
            cls_obj = globals()[lines[0]]
            new_instance = cls_obj()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """showing the string represent of an instance
        based on the classn name"""
        if not line:
            print("** class name missing **")
            return

        try:
            lines = line.split()
            clsObj = globals()[lines[0]]
            if len(lines) < 2:
                print("** instance id missing **")
                return

            newInstance = clsObj()
            instance_id = lines[1]
            key = f"{lines[0]}.{lines[1]}"
            objDIct = storage.all()
            if key in objDIct:
                print(objDIct[key])
            else:
                print("** no instance found **")
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """delete an instance based on the class name and id"""

        if not line:
            print("** class name missing **")
            return
        try:
            lines = line.split()
            clsObj = globals()[lines[0]]
            if len(lines) < 2:
                print("** instance id missing **")
                return

            newInstance = clsObj()
            instance_id = lines[1]
            key = f"{lines[0]}.{lines[1]}"
            objDIct = storage.all()
            if key in objDIct:
                del objDIct[key]
                storage.save()
            else:
                print("** no instance found **")
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, line):
        """show all string representation of all instance
        based or not based on the class"""

        objDict = storage.all()
        objList = []

        if not line:
            for key, value in objDict.items():
                objList.append(str(value))
            print(objList)
            return

        try:
            lines = line.split()
            clsObj = globals()[lines[0]]
            for key, value in objDict.items():
                objList.append(str(value))
            print(objList)
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        try:
            lines = line.split()
            cls_obj = globals()[lines[0]]

            if len(lines) < 2:
                print("** instance id missing **")
                return

            instance_id = lines[1]
            key = "{}.{}".format(lines[0], instance_id)
            obj_dict = storage.all()

            if key not in obj_dict:
                print("** no instance found **")
                return

            if len(lines) < 3:
                print("** attribute name missing **")
                return

            attr_name = lines[2]

            if len(lines) < 4:
                print("** value missing **")
                return
    
            attr_value = lines[3]
            obj = obj_dict[key]
            setattr(obj, attr_name, attr_value)
            obj.save()
        except KeyError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
