'''
https://www.jianshu.com/p/b5b8d488266e
'''
from typing import (
    Dict, List, Set, TypeVar, DefaultDict, Generic, Iterator, Set, Tuple, Union, Any
)
from collections import defaultdict
T = TypeVar('T')


class IdentityDict(Dict[T, T]):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __missing__(self, key: T) -> T:
        self[key] = key
        return key


class DisjointSet(Generic[T]):
    def __init__(self, *args, **kwargs) -> None:
        self._data: IdentityDict[T] = IdentityDict(*args, **kwargs)

    def __contains__(self, item: T) -> bool:
        return item in self._data

    def __bool__(self) -> bool:
        return bool(self._data)

    def __get__(self, e: T) -> T:
        return self.find(e)

    def __repr__(self) -> str:
        sets = {key: val for key, val in self}
        return f"{self.__class__.__name__} ({sets})"

    def __str__(self) -> str:
        return "{classname}({values})".format(
            classname=self.__class__.__name__, values=", ".join(
                str(dset) for dset in self.itersets()),
        )

    def __iter__(self) -> Iterator[Tuple[T, T]]:
        try:
            for key in self._data.keys():
                yield key, self.find(key)
        except RuntimeError as e:
            # raise BaseException() from e
            # print(e)
            pass

    def itersets(self, with_canonical_elements: bool = False) -> Iterator[Union[Set[T], Tuple[T, Set[T]]]]:
        element_classes: DefaultDict[T, Set[T]] = defaultdict(set)
        for element in self._data:
            element_classes[self.find(element)].add(element)
        if with_canonical_elements:
            yield from element_classes.items()
        else:
            yield from element_classes.values()

    def find(self, x: T) -> T:
        # 路径压缩 O(logn)
        while x != self._data[x]:
            self._data[x] = self._data[self._data[x]]
            x = self._data[x]
        return x

    def union(self, x: T, y: T) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            # 合并优化
            self._data[root_x] = root_y

    def connected(self, x: T, y: T) -> bool:
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    # dset = DisjointSet({1: 2, 2: 3})
    dset = DisjointSet()
    # dset.union(2,1)
    dset.union(1, 2)
    print(dset)
    print('connected(1, 2)', dset.connected(1, 2))
    print('connected(1, 3)', dset.connected(1, 3))
    print('find(1) root', dset.find(1))
