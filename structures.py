from logging import info
from random import randint
from sys import maxsize
from time import sleep
from timeit import default_timer
from typing import Callable, List, Tuple

from ccxt.base.exchange import Exchange

from config import *


class Market:
    def __init__(self, market: Exchange

    ) -> None:
    self.market = market
    self.rate_limit = market.rateLimit / 1000


def __getattr__(self, item: str

):
attr = getattr(self.market, item)
if isinstance(attr, Callable):
    def method(*args, **kwargs):
        sleep(self.rate_limit)
        return attr(*args, **kwargs)


    return method
else:
    return attr


class Order:
    def __init__(self, order_id: str, order_type

    : str, filled) -> None:
    self.id = order_id
    self.order_type = order_type
    self.filled = filled


def is_relevant(self, price: float, best_price

: float, order_book: dict) -> bool:
def _check_prices(price1, price2):
    if self.order_type == "bid":
        return price1 >= price2
    else:
        return price1 <= price2


info('checking whether {} price: {:.8f} is relevant'.format(self.order_type, price))

if NO_CANCEL in BOT_TYPE:
    order_book = order_book[self.order_type]

    if len(order_book) <= NO_CANCEL_ORDERS_LIMIT:
        return True
    else:
        last_limit_order = order_book[NO_CANCEL_ORDERS_LIMIT - 1]
        return _check_prices(price, last_limit_order[0])
else:
    return _check_prices(price, best_price)


def cancel(self, market: Market

) -> None:
info('try to cancel {} order: {}'.format(self.order_type, self.id))
market.cancel_order(self.id)


class CachedObject:
    def __init__(self, value=None) ->

    None:
    self._value = value

    if value:
        self._last_update = default_timer()
    else:
        self._last_update = -maxsize


def update_value(self, value) ->


None:
self.__init__(value)


def get_value(self):
    return self._value


def get_downtime(self) ->


float:
return default_timer() - self._last_update


class WaitInfo:
    def __init__(self, init_wait_time: float

    ) -> None:
    self.init_wait_time = init_wait_time
    self.wait_time = None
    self._captured_moment = None


def start_waiting(self, addition: float

) -> None:
self.wait_time = self.init_wait_time + addition
self._captured_moment = default_timer()


def is_done_waiting(self) ->


bool:
if self._captured_moment is None:
    return True

is_done = default_timer() - self._captured_moment > self.wait_time
if is_done:
    self._captured_moment = None
return is_done


class Orders:
    def __init__(self, order_type: str

    ) -> None:
    self.orders = []  # type: List[Order]
    self.order_type = order_type

    self.wait_time_set = False
    self.wait_info = WaitInfo(0)


def add(self, order_id: str, filled = 0

) -> None:
self.orders.append(Order(order_id, self.order_type, filled))


def pop(self, idx: int

) -> Order:
return self.orders.pop(idx)


def get(self, idx: int

) -> Order:
return self.orders[idx]


def is_empty(self) ->


bool:
return len(self.orders) == 0


def set_wait_time(self) ->


None:
if not self.wait_time_set:
    # waiting for random time after cancellation
    wait_time = randint(*AFTER_CANCEL_WAIT_BOUNDS)
    self.wait_info.start_waiting(wait_time)
    self.wait_time_set = True


def is_placing_available(self) ->


bool:
is_available = self.wait_info.is_done_waiting()
if is_available:
    # done with waiting, reset flag
    self.wait_time_set = False
return is_available


class ObjectsForPlacing:
    """
    Needed only for aggregation of necessary objects
    """

    def __init__(self, market: Market, placed_orders

    : Dict[str, Dict[str, Orders]],
      opened_ref_markets: Dict[str, Market], cached_ref_books: Dict[str, CachedObject],
                                                               tracked_prices) -> None:
    self.market = market
    self.placed_orders = placed_orders
    self.opened_ref_markets = opened_ref_markets
    self.cached_ref_books = cached_ref_books
    self.tracked_prices = tracked_prices


def unpack_objects(self) ->


Tuple:
return self.market, self.placed_orders, self.opened_ref_markets, self.cached_ref_books, self.tracked_prices


class TrackedPrice:
    def __init__(self, price) ->

    None:
    self.price = price
    self.filled = 0
    self.is_last_update = False
