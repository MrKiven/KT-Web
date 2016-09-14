# -*- coding: utf-8 -*-

import threading
import functools


def run_in_thread(t_name):
    """Wrapper a func run as a thread"""
    def decorator(func):
        @functools.wraps(func)
        def guard(*a, **k):
            func_hl = threading.Thread(target=func, args=a, kwargs=k)
            func_hl.setName(t_name)
            func_hl.start()
            return func_hl
        return guard
    return decorator


class Event(object):
    """Event Object"""

    def __init__(self, func, stop_event):
        self.func = func
        self.stop_event = stop_event
        self.is_running = False

    @property
    def name(self):
        return self.func.__name__

    def trigger(self):
        if self.is_running:
            return
        if callable(self.func):
            run_in_thread(self.name)(self.func)(self.stop_event)
            self.is_running = True


class EventManager(object):
    """Events manager

    Example:

        from kt_web.event_manager import event_manager

        def task(stop_event):
            while not stop_event.is_set():
                do_stuff()

        event_manager.clear_event()  # clear all events already exists
        event_manager.register(task)
        event_manager.trigger(task)  # or `event_manager.trigger_all()`

        # here is gunicorn's main loop...
        # After some condition you want to stop event, just do:
        event_manager.set_event()

    """

    def __init__(self):
        self.stop_event = threading.Event()
        self.events = {}
        self.events_name = []

    def register(self, func):
        """Same function or method name only register once.
        """
        if func.__name__ not in self.events_name:
            self.events[func] = Event(func, self.stop_event)
            self.events_name.append(func.__name__)

    def __getitem__(self, func):
        try:
            return self.events[func]
        except KeyError:
            return None

    def trigger(self, func):
        self[func].trigger()

    def trigger_all(self):
        for func in self.events:
            self.trigger(func)

    def clear(self):
        self.events.clear()

    def clear_event(self):
        self.stop_event.clear()

    def set_event(self):
        """Stop all events"""
        self.stop_event.set()  # set event True

event_manager = EventManager()
