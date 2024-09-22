
from plyer import notification
import time

while True:
    notification.notify(
        title = 'reminder',
        message = 'this is a dummy reminder',
        timeout = '5',
    )

    

    time.sleep(10)