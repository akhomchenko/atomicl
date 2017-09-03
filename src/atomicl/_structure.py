import abc

from atomicl._compat import ABC


class AtomicLong(ABC):
    @property
    @abc.abstractmethod
    def value(self):
        """
        Returns the current value

        :return int: the current value
        """

    @value.setter
    @abc.abstractmethod
    def value(self, new_value):
        """
        Sets to the given value

        :param int new_value: the value to be set
        :rtype: None
        """

    @abc.abstractmethod
    def __iadd__(self, other):
        """
        Atomically adds the given value to the current value

        :param int other: the value to add
        :rtype: AtomicLong
        """

    @abc.abstractmethod
    def __isub__(self, other):
        """
        Atomically subs the given value from the current value

        :param int other: the value to sub
        :rtype: AtomicLong
        """

    @abc.abstractmethod
    def get_and_set(self, new_value):
        """
        Atomically sets to the given value and returns the old value

        :param int new_value: the value to be set
        :return: the old value
        :rtype: int
        """

    def compare_and_set(self, expected_value, new_value):
        """
        Atomically sets to the given value if the current value is
        equal to the expected value

        :param int expected_value: the expected value
        :param new_value: the value to be set
        :return: `True` if successful. `False` indicates that
        the current value was not equal to the expected
        :rtype: bool
        """
