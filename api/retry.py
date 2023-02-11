import time
from functools import wraps
from logging import Logger, getLogger
from typing import List

from requests import HTTPError


def retry(
    max_attempts: int = 3, 
    initial_delay_ms: int = 500, 
    transient_error: Exception = HTTPError,
    http_error_code: List[int] = [429, 500, 502, 503, 524],
    logger: Logger = getLogger(__name__)
):
    """Retry decorator that re-calls the decorated function when transient error happens
    Specifically, when transient error is HTTPError, only the specified error code will be
    excepted and retried. For each retry, the delay time will increase exponentially.

    Args:
        max_attempts (int, optional): maximum attempts to retry. Defaults to 3.
        initial_delay_ms (int, optional): initial delay between the first and second call. Defaults to 500.
        transient_error (Exception, optional): the transient error to except and retry. Defaults to HTTPError.
        http_error_code (List[int], optional): if transient error is HTTPError,
            this specifies the status code to catch and retry. Defaults to [429, 500, 502, 503, 524].
        logger (Logger, optional): logging.Logger style. Defaults to default logger.
    """
    def decorator(func):
        """ this is the actual decorator that decorates the target function """
        @wraps(func)
        def inner(*args, **kwargs):
            """ inner is the target function that is decorated """
            delay = initial_delay_ms / 1000
            # try calling func for a maximum of max_attempts times
            for _ in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except transient_error as e:
                    # case when transient error is HTTPError but error code is not in the given error code list
                    if isinstance(e, HTTPError) and e.response.status_code not in http_error_code:
                        raise e
                    # otherwise display error message, sleep, and double the delay
                    msg = f"Exception '{e}' occurred when calling {func.__name__}. Retry in {delay} seconds ..."
                    logger.exception(msg)
                    time.sleep(delay)
                    # TODO: add jitter -see: https://aws.amazon.com/cn/blogs/architecture/exponential-backoff-and-jitter/
                    delay = delay * 2
                    error = e

            raise error
        return inner
    return decorator
