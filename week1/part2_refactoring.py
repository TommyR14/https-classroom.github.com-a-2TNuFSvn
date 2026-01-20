import time


def follower(sensor_values):
    left_speed = sensor_values[0]
    center = sensor_values[1]
    right_speed = sensor_values[2]
    if center > 0.5:
        error = 0
    elif left_speed > 0.5:
        error = -1
    else:
        error = 1
    kp = 0.5
    kd = 0.2
    global prev_e
    output = kp * error + kd * (error - prev_error)
    prev_error = error
    base_speed = 1.0
    left_motor = base_speed - output
    right_motor = base_speed + output
    return left_motor, right_motor


prev_error = 0
sensor_values = [0.1, 0.8, 0.1]
for i in range(100):
    left_speed, right_speed = follower(sensor_values)
    print(f"L:{left_speed},R:{right_speed}")
    time.sleep(0.01)
