def damage(damage, speed, time):
    times = {"second": 1, "minute": 60, "hour": 3600}
    if damage < 0 or speed < 0:
        return "invalid"
    return int(damage * speed * times[time])
