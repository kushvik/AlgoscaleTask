from twitter import *

t = Twitter(
    auth=OAuth("770886120707993600-VQmi2D22JCKQnQRQOchPKo2JxYSsCOH", "dc3CRC4YZtBVvtiO61k8ZYhARhNqX3R5ix876BtjEZYu8" , "nekBfNyTHoxu5x01uuI2UMaoH", "dkOM1ikappRZON2K4z6wL0ekb54nKPuxW0TvdHaulSpes5X16v" ))

# Get your "home" timeline
print(t.statuses.home_timeline())