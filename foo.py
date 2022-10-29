
class Tracker(ABC):
    """Tracks the position of an object over time."""


    @abstractmethod
    def start_new_descent(self):
        """Signals to the tracker that a new descent is beginning."""
        ...

    @abstractmethod
    def update(self, observation):
        """Updates the tracker's estimate of the object's current position, based on a new observation.

        Parameters
        ----------
        observation : float
            A sensor observation of the object's current position

        Returns
        -------
        float
            the tracker's estimate of the object's current position
        """
        ...


class SensorBasedTracker(Tracker):
    """A Tracker that completely trusts
       its sensor observations."""

    def __init__(self):
        pass

    def start_new_descent(self):
        pass

    def update(self, observation):
        return observation



