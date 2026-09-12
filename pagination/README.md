# Pagination

This project covers pagination techniques in Python, including simple pagination, hypermedia pagination, and deletion-resilient hypermedia pagination.

## Tasks

### 0. Simple helper function

Implement `index_range(page, page_size)` to calculate the start and end indexes for a pagination range.

### 1. Simple pagination

Implement a `Server` class that loads the `Popular_Baby_Names.csv` dataset and provides a `get_page` method to return a specific page of the dataset.

The dataset is cached after the first load.

### 2. Hypermedia pagination

Extend the pagination functionality with a `get_hyper` method.

The method returns:

* `page_size`
* `page`
* `data`
* `next_page`
* `prev_page`
* `total_pages`

The implementation reuses `get_page`.

### 3. Deletion-resilient hypermedia pagination

Implement `get_hyper_index` to paginate using indexes that remain meaningful when rows are deleted between queries.

The method returns:

* `index`
* `next_index`
* `page_size`
* `data`

The dataset is indexed using `indexed_dataset()` to make pagination resilient to deletions.

## Files

* `0-simple_helper_function.py` - Helper function for calculating pagination indexes.
* `1-simple_pagination.py` - Basic pagination implementation.
* `1-main.py` - Tests for simple pagination.
* `2-hypermedia_pagination.py` - Hypermedia pagination implementation.
* `2-main.py` - Tests for hypermedia pagination.
* `3-hypermedia_del_pagination.py` - Deletion-resilient hypermedia pagination.
* `3-main.py` - Tests for deletion-resilient pagination.
* `Popular_Baby_Names.csv` - Dataset used by the pagination classes.

## Requirements

* Python 3
* `Popular_Baby_Names.csv`


