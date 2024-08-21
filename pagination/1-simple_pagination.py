#!/usr/bin/env python3
"""A module that paginates a dataset of popular baby names."""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing a start and end index."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cache the dataset after loading it from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude the header row.

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page from the dataset."""
        # Assert that both arguments are integers greater than 0
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        # Get the start and end indices
        start_index, end_index = index_range(page, page_size)

        # Retrieve the dataset
        dataset = self.dataset()

        # If the start index is out of range, return an empty list
        if start_index >= len(dataset):
            return []

        # Return the appropriate slice of the dataset
        return dataset[start_index:end_index]
