def load_settings():
    settings = {}
    with open('settings.txt') as f:
        for line in f:
            (key, val) = line.split('=')
            settings[key] = val
    return settings