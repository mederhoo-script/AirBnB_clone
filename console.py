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

    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
        ]

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
        based on the class name"""
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

    def precmd(self, line):
        if "(" in line:
            line = line.replace("(", "")
        if ")" in line:
            line = line.replace(")", "")

        if "." in line:
            lines = line.split(".")

            if "{" in lines[1]:
                    lines[1] = lines[1].replace("{", "")

            if "}" in lines[1]:
                lines[1] = lines[1].replace("}", "")


            if '"' in lines[1]:
                lines[1] = lines[1].replace('"', " ")

                if "'" in lines[1]:
                    lines[1] = lines[1].replace("'", " ")

                if "," in lines[1]:
                    lines[1] = lines[1].replace(",", "")

                if ":" in lines[1]:
                    lines[1] = lines[1].replace(":", "")

                lines[1] = lines[1].split()

                if len(lines[1]) > 5:
                    li3to5 = f"{lines[1][3]} {lines[1][4]} {lines[1][5]}"
                    comd = f"{lines[1][0]} {lines[0]} {lines[1][1]} {lines[1][2]} {li3to5}"
                    return super().precmd(comd)

                elif len(lines[1]) > 3:
                    comd = f"{lines[1][0]} {lines[0]} {lines[1][1]} {lines[1][2]} {lines[1][3]}"
                    return super().precmd(comd)

                elif lines[1][1]:
                    comd = f"{lines[1][0]} {lines[0]} {lines[1][1]}"   
                    print(f"line ; {line} str: {str} out: {lines}")
                    return super().precmd(comd)

            if "'" in lines[1]:
                lines[1] = lines[1].split("'", " ")

                if '"' in lines[1]:
                    lines[1] = lines[1].replace('"', " ")

                if "," in lines[1]:
                    lines[1] = lines[1].replace(",", "")

                if ":" in lines[1]:
                    lines[1] = lines[1].replace(":", "")


                lines[1] = lines[1].split()
                if len(lines[1]) > 5:
                    li3to5 = f"{lines[1][3]} {lines[1][4]} {lines[1][5]}"
                    comd = f"{lines[1][0]} {lines[0]} {lines[1][1]} {lines[1][2]} {li3to5}"
                    return super().precmd(comd)

                elif len(lines[1]) > 3:
                    comd = f"{lines[1][0]} {lines[0]} {lines[1][1]} {lines[1][2]} {lines[1][3]}"
                    return super().precmd(comd)

                elif lines[1][1]:
                    comd = f"{lines[1][0]} {lines[0]} {lines[1][1]}"   
                    print(f"line ; {line} str: {str} out: {lines}")
                    return super().precmd(comd)
                    
            comd = f"{lines[1]} {lines[0]}"
            return super().precmd(comd)
        else:
            return super().precmd(line)
        
        # def default(self, arg):
    #     """
    #     cmd method to validate when it does not
    #     recognize the prefix of the command.
    #     """
    #     args = arg.split(".")
    #     separator = args[1].split("(")
    #     new_separator = separator[1].split(")")
    #     new = new_separator[0].split(",")
    #     if args[0] in self.__classes:
    #         if args[1] == "all()":
    #             nameClass = args[0]
    #             return self.do_all(nameClass)
    #         elif args[1] == "count()":
    #             nameClass = args[0]
    #             return self.do_count(nameClass)
    #         elif args[1][0:4] == 'show':
    #             arguments = args[0] + " " + new_separator[0]
    #             return self.do_show(arguments)
    #         elif args[1][0:7] == 'destroy':
    #             arguments = args[0] + " " + new_separator[0]
    #             return self.do_destroy(arguments)
    #         elif args[1][0:6] == "update":
    #             arguments = args[0] + " " + new[0] + "" + new[1] + "" + new[2]
    #             return self.do_update(arguments)

    
    def do_all(self, line):
        """show all string representation of all instance
        based or not based on the class"""

        objList = []
        try:
            lines = line.split()
            if not lines:
                for key, value in storage.all().items():
                    objList.append(str(value))
            else:
                clsObj = globals()[lines[0]]
                for key, value in storage.all().items():
                    if isinstance(value, clsObj):
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
            if len(lines) > 5:
                attr_age = lines[4]
                attr_age_value = lines[5]

                setattr(obj, attr_age, attr_age_value)
            obj.save()
        except KeyError:
            print("** class doesn't exist **")


    def do_count(self, arg):
        """Instance counter according to class"""
        args = arg.split(" ")
        if arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            list_new = []
            list_dictionary = storage.all()
            for key, value in list_dictionary.items():
                if args[0] in key:
                    list_new.append(value)
            print(len(list_new))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
