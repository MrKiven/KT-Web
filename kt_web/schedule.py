# -*- coding: utf-8 -*-

import gevent
import gevent.event


class Schedule(object):
    """Schedule Object"""

    def __init__(self, func, stop_event):
        self.func = func
        self.stop_event = stop_event
        self.g = None

    @property
    def name(self):
        return self.func.__name__

    def trigger(self):
        if not self.g and callable(self.func):
            self.g = gevent.spawn(self.func, self.stop_event)

    def stop(self):
        if self.g:
            gevent.kill(self.g)


class ScheduleManager(object):
    """Schedules Manager

    Example:

        from zeus_core.schedule import schedule_manager

        def task(stop_event):
            while not stop_event.is_set():
                do_stuff()

        schedule_manager.clear_schedules()  # clear all exist schedules
        schedule_manager.add(task)
        schedule_manager.trigger(task)  # or `event_manager.trigger_all()`

        # here is gunicorn's main loop...
        # After some condition you want to stop *task* schedule, just do:
        schedule_manager.stop(task) # or `schedule_manager.set_events()` to
        stop all schedules

    Generally, all schedules will stop after gunicorn master stop.

    Note:
      In *task* func, there must be IO operation or `gevent.sleep()` explicitly
      to switch greenlet.

    """

    def __init__(self):
        """Schedules Manager
        Initialize a global *gevent.event.Event* to manager all greenlets.
        Initialize a dict to store all events registered.
        """
        self.stop_event = gevent.event.Event()
        self.schedules = {}

    def add(self, func):
        """Same function only register once"""
        if func not in self.schedules:
            self.schedules[func] = Schedule(func, self.stop_event)

    def trigger(self, func):
        """Trigger given func to run as a greenlet"""
        self.schedules[func].trigger()

    def trigger_all(self):
        """Trigger all func in manager to run"""
        for func in self.schedules:
            self.trigger(func)

    def clear(self):
        """Clear schedules in manager"""
        self.schedules.clear()

    def clear_schedules(self):
        """Set *gevent.event.Event* False"""
        self.stop_event.clear()

    def stop(self, func):
        """Stop given func schedule"""
        self.schedules[func].stop()

    def set_events(self):
        """Stop all schedules"""
        if not self.stop_event.is_set():
            self.stop_event.set()  # set event True

schedule_manager = ScheduleManager()
