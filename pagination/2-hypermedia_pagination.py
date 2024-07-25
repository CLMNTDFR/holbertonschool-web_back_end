#!/usr/bin/env python3
"""  a method named get_page that takes
two integer arguments page with default
value 1 and page_size with default value 10"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """return a tuple of size two
    containing a start index and an
    end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ takes two integer arguments page with
        default value 1 and page_size with
        default value 10"""
        assert type(page) == int or type(page_size) == int
        assert page > 0 or page_size > 0
        mydataset = self.dataset()
        indexes = index_range(page, page_size)
        dataset_length = len(mydataset)

        if indexes[0] < dataset_length and indexes[1] <= dataset_length:
            return mydataset[indexes[0]:indexes[1]]

        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """takes the same arguments (and defaults) as get_page
        and returns a dictionary containing the following key-value
        pairs"""
        mydataset = self.dataset()
        data = self.get_page(page, page_size)
        page_size = len(data)
        total_pages = len(mydataset)
        result = self.get_page(page + 1, page_size)
        if result == []:
            next_page = None
        else:
            next_page = page + 1

        result = self.get_page(page - 1, page_size)
        if result == []:
            previous_page = None
        else:
            previous_page = page - 1

        return {"page_size": page_size,
                "page": page, "data": data,
                "next_page": next_page,
                "prev_page": previous_page,
                "total_pages": total_pages}
