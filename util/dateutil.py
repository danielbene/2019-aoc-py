from datetime import datetime

# modify pattern to match your date locale
tsPattern = '%Y-%m-%d %H:%M:%S.%f'


def current_timestamp() -> float:
    return datetime.strptime(str(datetime.now()), tsPattern).timestamp()
