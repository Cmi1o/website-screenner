import constants


def next_page_url(base_url: str, page_number: int) -> str:
    return base_url + constants.NEXT_PAGE_ENDPOINT.format(page_number)
