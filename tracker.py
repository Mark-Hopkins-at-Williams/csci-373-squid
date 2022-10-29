from abc import ABC, abstractmethod
from numpy.random import normal


class MotionModel:
    """A model of motion with normally distributed noise.

    Each time step, the object travels a distance of D, where D is a sample from
    a normal distribution with mean M.
    """

    def __init__(self, velocity_mean, velocity_noise):
        """
        Parameters
        ----------
        velocity_mean : float
            The mean velocity of the object
        velocity_noise : float
            The standard deviation of the normal distribution from which we draw the distance
            traveled each time step.
        """

        self.velocity_mean = velocity_mean
        self.velocity_noise = velocity_noise

    def move(self, current_position):
        """Moves from the current position to the next position, according to the motion model.

        Parameters
        ----------
        current_position : float
            The position of the object, prior to moving

        Returns
        -------
        float
            the position of the object, after moving
        """

        return current_position + normal(loc=self.velocity_mean, scale=self.velocity_noise)

    def get_average_velocity(self):
        """Returns the average velocity."""
        return self.velocity_mean

    def get_velocity_noise(self):
        """Returns the standard deviation of the velocity."""
        return self.velocity_noise


class Sensor:
    """A noisy position sensor.

    Given an object's true position P, the sensed position is drawn from a normal distribution
    with mean P.
    """

    def __init__(self, sensor_noise):
        """
        Parameters
        ----------
        sensor_noise : float
            The standard deviation of the normal distribution from which we draw the sensor observation
        """

        self.sensor_noise = sensor_noise

    def sense(self, true_position):
        """Returns a noisy observation of the object's true position.

        Parameters
        ----------
        true_position : float
            The object's true position.

        Returns
        -------
        float
            The sensed position, drawn from a normal distribution whose mean is the true position,
            and whose standard deviation is defined by self.sensor_noise.
        """

        return normal(loc=true_position, scale=self.sensor_noise)

    def get_sensor_noise(self):
        """Returns the standard deviation of the sensor observations."""
        return self.sensor_noise



def simulate_trajectory(motion_model, starting_position, finish_line):
    """Simulates a trajectory with a MotionModel.

    Given a starting position, this function should simulate a series of moves from
    a MotionModel, until it exceeds a threshold. It should then return the list
    of object positions at each time step (in order) of its travel, beginning with the
    starting position.

    Parameters
    ----------
    motion_model : MotionModel
        The motion model.
    starting_position : float
        The starting position of the object
    finish_line : float
        The threshold that the object needs to reach (or exceed)

    Returns
    -------
    list[float]
        The sequence of object positions at each time step, beginning with the starting position.
    """
    # question one


def track_trajectory(trajectory, sensor, trackers):
    """Tracks a trajectory using a set of trackers.

    A trajectory is a sequence of an object's true position at each time step.

    The trackers are provided as a dictionary that maps strings (the trackers' names) to
    a Tracker instance.

    At each time step of the trajectory, this function uses the sensor to get a reading
    ("observation") of the object's position at that time step. It then reports this
    observation to each tracker, who update their estimate of the object's position.

    The function should return two dictionaries:
    - the first dictionary should map each tracker's name to its sequence of position
      estimates
    - the second dictionary should map each tracker's name to its absolute error at each
      time step, i.e. the absolute difference between its position estimate and the object's
      true position

    Parameters
    ----------
    trajectory : list[float]
        A sequence containing the object's true positions at each time step
    sensor : Sensor
        A position sensor
    trackers : dict[str, Tracker]
        A dictionary that maps strings (the tracker's name) to a Tracker instance

    Returns
    -------
    dict[str, list[float]], dict[str, list[float]]
        Two dictionaries. The first dictionary should map each tracker's name to its sequence
        of position estimates. The second dictionary should map each tracker's name to its
        absolute error at each time step, i.e. the absolute difference between its position
        estimate and the object's true position.
    """
    # question two


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
    """A Tracker that completely trusts its sensor observations."""

    def __init__(self):
        pass

    def start_new_descent(self):
        """Signals to the tracker that a new descent is beginning."""
        pass

    def update(self, observation):
        """Updates the tracker's estimate of the object's current position to match the latest observation.

        Parameters
        ----------
        observation : float
            A sensor observation of the object's current position

        Returns
        -------
        float
            the tracker's estimate of the object's current position, which is just the latest observation
        """
        ...
        return observation


class VelocityBasedTracker(Tracker):
    """A Tracker that assumes the object travels at a constant velocity.

    In other words, it assumes the object travels the exact same distance during every time step.
    """

    def __init__(self, start_position, motion_model):
        """
        Parameters
        ----------
        start_position : float
            The starting position of the object.
        motion_model : MotionModel
            A model of the object's motion during each time step
        """
        # question three

    def start_new_descent(self):
        """Signals to the tracker that a new descent is beginning."""
        # question three

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
        # question three


class KalmanTracker(Tracker):
    """A Tracker that tracks an object using a Kalman filter."""

    def __init__(self, start_position, motion_model, sensor):
        """
        Parameters
        ----------
        start_position : float
            The starting position of the object.
        motion_model : MotionModel
            A model of the object's motion during each time step
        sensor : Sensor
            The sensor that makes observations of the object's position at each time step
        """
        # question four

    def start_new_descent(self):
        """Signals to the tracker that a new descent is beginning."""
        # question four

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
        # question four
