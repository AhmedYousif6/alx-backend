#!/usr/bin/env python3
""" task 0"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return the index range from a given page and page size"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
