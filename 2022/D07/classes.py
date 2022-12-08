from typing import Union


tab_size: int = 4


class File:
    __name: str
    __size: int
    __count: int
    __parent: "Dir"

    def __init__(self: "File", name: str, size: int, parent: "Dir") -> None:
        self.__name = name
        self.__size = size
        self.__count = 1
        self.__parent = parent

    @staticmethod
    def from_size(name: str, size: int) -> "File":
        return File(name, size, None)

    @staticmethod
    def from_name(name: str) -> "File":
        return File(name, 0, None)

    def __str__(self: "File") -> str:
        return self.pretty_print(0)

    def pretty_print(self: "File", depth: int) -> str:
        global tab_size
        ret: str = " " * tab_size * depth
        ret += "- " + self.__name + \
            " (file, size = " + str(self.__size) + ")\n"
        return ret

    def name(self: "File") -> str:
        return self.__name

    def size(self: "File") -> int:
        return self.__size

    def count(self: "File") -> int:
        return self.__count

    def parent(self: "File") -> "Dir":
        return self.__parent


class Dir:
    __name: str
    __parent: "Dir"
    __children: dict[str, Union["Dir", "File"]]

    def __init__(self: "Dir", name: str, parent: "Dir", children: dict[str, Union["Dir", "File"]]) -> None:
        self.__name = name
        self.__parent = parent
        self.__children = children

    @staticmethod
    def from_parent(name: str, parent: "Dir") -> "Dir":
        return Dir(name, parent, {})

    @staticmethod
    def from_name(name: str) -> "Dir":
        return Dir(name, None, {})

    def __str__(self: "Dir") -> str:
        return self.pretty_print(0)[:-1]

    def pretty_print(self: "Dir", depth: int) -> str:
        global tab_size
        ret: str = " " * tab_size * depth
        ret += "- " + self.__name + " (dir, size = " + str(self.size()) + ")\n"

        for child in self.__children.values():
            pnt = child.pretty_print(depth + 1)
            if (pnt == None):
                ret += "\n"
            else:
                ret += pnt

        return ret

    def name(self: "Dir") -> str:
        return self.__name

    def parent(self: "Dir") -> "Dir":
        return self.__parent

    def children(self: "Dir") -> dict[str, Union["Dir", "File"]]:
        return self.__children

    def size(self: "Dir") -> int:
        return sum(child.size() for child in self.__children.values())

    def count(self: "Dir") -> int:
        return sum(child.count() for child in self.__children.values())

    def add(self: "Dir", child: Union["Dir", "File"]) -> None:
        self.__children[child.name()] = child

    def get(self: "Dir", path: str) -> Union["Dir", "File"]:
        if (path == "."):
            return self
        if (path == ".."):
            return self.__parent
        if (path in self.__children):
            return self.__children[path]

        return None
