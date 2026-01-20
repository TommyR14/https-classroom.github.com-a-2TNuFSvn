import time


def calculate_line_error(left, center, right, threshold):
    if left > threshold:
        error = -1
    elif center > threshold:
        error = 0
    elif right > threshold:
        error = 1
    return error


def compute_pd_output(error, previous_error, kp=0.5, kd=0.2):
    correction = kp * error + kd * (error - previous_error)
    return correction


def calculate_motor_speeds(base_speed, correction):
    left_motor = base_speed - correction
    right_motor = base_speed + correction
    return left_motor, right_motor


def control_step(sensor_values, previous_error, base_speed=0.1):
    left, center, right = sensor_values
    error = calculate_line_error(left, center, right)
    correction = compute_pd_output(error, previous_error)
    left_speed, right_speed = calculate_motor_speeds(base_speed, correction)
    return left_speed, right_speed, error
