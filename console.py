#!/usr/bin/python3
"""module console that contains the entry point
of the command interpreter"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit Command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True

    def emptyline(self):
        """Empty lines are ignored"""
        pass

    def do_create(self, text):
        """Creates an instance
            Usage: create <class name>
        """
        args = text.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0] + '()')
            models.storage.save()
            print(new_instance.id)

    def do_show(self, text):
        """Prints the string representation of an instance
            Usage: show <class name> <id>"""
        args = text.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in obj:
                print("** no instance found **")
            else:
                print(obj[key])

    def do_destroy(self, text):
        """ Deletes an instance
            Usage: destroy <class name> <id>
        """
        args = text.split()
        obj = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in obj:
                print("** no instance found **")
            else:
                del obj[key]
                storage.save()

    def do_all(self, text):
        """Prints all string representation of all instances
            Usage: all <class name>
        """
        args = text.split()
        objects = models.storage.all()
        new_list = []
        if len(args) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, text):
        """Updates an instance
            Usage update <class name> <id> <attribute name> '<attribute value>'
        """
        objects = models.storage.all()
        args = text.split(" ")

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = objects.get(key, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
