FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """Read text files and return the list of
    todo items.
    """
    with open(filepath, "r") as file_local:
       todos_local = file_local.readlines()
       """Write the to-do items list in a text file."""
    return todos_local

def write_todos(todos_arg,filepath = FILEPATH):
    with open(filepath,"w") as file:
      file.writelines(todos_arg)
 
if __name__ == "__main__":
    print("welcome to the modules")