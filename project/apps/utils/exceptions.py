from urllib.error import HTTPError


class ExchangeRateResponseError(HTTPError):
    pass


class SearchResultResponseError(HTTPError):
    pass