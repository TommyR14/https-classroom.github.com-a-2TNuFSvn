from typing import Tuple

"""Returns error based on which direction is greater than the threshold"""
def calculate_line_error(left, center, right, threshold) -> float:
    if left > threshold:
        error = -1
    elif center > threshold:
        error = 0
    elif right > threshold:
        error = 1
    return error


"""Calculate correction based on given kp and kd as well as what the error and previous error will be"""
def compute_pd_output(error, previous_error, kp=0.5, kd=0.2) -> float:
    correction = kp * error + kd * (error - previous_error)
    return correction


"""Takes input base speed and correction values, returns speed of left or right motor by doing +/-"""
def calculate_motor_speeds(base_speed, correction) -> Tuple[float, float]:
    left_motor = base_speed - correction
    right_motor = base_speed + correction
    return left_motor, right_motor


"""Sets values to variables, returns the left and right motor speeds as well as error values"""
def control_step(
    sensor_values, previous_error, base_speed=0.1) -> Tuple[float, float, int]:
    left, center, right = sensor_values
    error = calculate_line_error(left, center, right, threshold)
    correction = compute_pd_output(error, previous_error)
    left_speed, right_speed = calculate_motor_speeds(base_speed, correction)
    return left_speed, right_speed, error
