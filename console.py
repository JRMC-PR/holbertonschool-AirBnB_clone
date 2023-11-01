#!/usr/bin/env python3
"""This module contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that contains the entry point of the command"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        Args:
            arg (str): arguments coming from the command line"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        Args:
            arg (str): arguments coming from the command line"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id
        Args:
            arg (str): <class name>"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in globals():
            print("** class doesn't exist **")
            return
        else:
            # & create a new instance of the class
            # & arg is the class name
            new_instance = globals()[arg]()
            new_instance.save()  # & save the new instance
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of
        an instance based on the class
        name and id
        Args:
            arg (str): <class name> <id>
        """
        args = arg.split()  # & split the arguments into a list of strings
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in globals() or not \
                issubclass(globals()[args[0]], BaseModel):
            # & checks if the clas name exist in the globals
            # & globals being a dictionary of all the classes
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]  # & key is the class name + id
        if key in storage.all():  # & storage.all() is a dict wiht inst
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the
        class name and id (save the change
        into the JSON file)
        Args:
            arg (str): <class name> <id>
        """
        args = arg.split()  # & split the arguments into a list of strings
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in globals() or not \
                issubclass(globals()[args[0]], BaseModel):
            # & checks if the clas name exist in the globals
            # & globals being a dictionary of all the classes
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]  # & key is the class name + id
        if key in storage.all():  # & storage.all() is a dict wiht inst
            del storage.all()[key]  # & delete the instance with the key
            storage.save()  # & save the changes to the json file
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of
        all instances based or not on the
        class name
        Args:
            arg (str): <class name>
        """
        args = arg.split()  # & split the arguments into a list of strings
        if len(args) == 0:
            # & if there are no arguments
            # & print all the instances
            for key, obj in storage.all().items():
                print(obj)
        else:
            key = args[0]
            if key not in globals() or not \
                    issubclass(globals()[key], BaseModel):
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                # & storage.all() is a dict wiht inst
                # & items() key values pairs tuple
                if key.split(".")[0] == args[0]:
                    print(obj)

    def do_update(self, arg):
        """Updates an instance based on the
        class name and id by adding or
        updating attribute (save the change
        into the JSON file)
        Args:
            arg (str): <class name> <id> <attribute name> <attribute value>
        """
        args = arg.split()
        #
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in globals() or not \
                issubclass(globals()[args[0]], BaseModel):
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        key = args[0] + "." + args[1]
        if key in storage.all():
            setattr(storage.all()[key], args[2], args[3])
            storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
