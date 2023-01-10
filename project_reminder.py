import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = " ** Please drink water now !",
            message = " Please drink water for your health, Daily you want to drink 3 to 4 lit water for your body",
            timeout = 45
        )
        time.sleep(60*60)    
