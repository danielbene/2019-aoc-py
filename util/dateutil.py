from datetime import datetime

# modify pattern to match your defaults
tsPattern = '%Y-%m-%d %H:%M:%S.%f'


def current_formatted_timestamp():
    return datetime.strptime(str(datetime.now()), tsPattern).timestamp()
