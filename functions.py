FILENAME = "todos.txt"


def get_item_number(item_list) -> int:
    position = int(input('Enter the item number to edit/complete: '))
    if position < 1 or position > len(item_list):
        print("The index can't be less than 1 or greater than the list of items."
              "Please try again!")
        return -1
    return position


def read_file_contents(filename=FILENAME) -> [str]:
    """
    Reads text file contents
    :param filename: File path
    :return: Returns lines of a file as a list
    """
    with open(filename, 'r') as file_obj:
        return file_obj.readlines()


def write_file_contents(content: [str], filename=FILENAME) -> None:
    """
    Writes to a text file
    :param content: Lines to be written
    :param filename: File path
    :return: None
    """
    with open(filename, 'w') as file_obj:
        file_obj.writelines(content)


# print(f"Module name: {__name__}")
if __name__ == "__main__":
    print(read_file_contents())
