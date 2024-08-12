def make_readable(seconds):
    time = []
    if seconds >= 0:
        hours = seconds // 3600
        minutes = (seconds % 3600) / 60
        second = (seconds % 3600) % 60

        if hours < 10:
            time.append("0" + str(int(hours)))
        else:
            time.append(str(int(hours)))
        if minutes < 10:
            time.append("0" + str(int(minutes)))
        else:
            time.append(str(int(minutes)))
        if second < 10:
            time.append("0" + str(int(second)))
        else:
            time.append(str(int(second)))

    return ":".join(time)

print(make_readable(59))