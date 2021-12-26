
from datetime import datetime
today = datetime.now()
from operations import balenq
def sl():
    print("-"*50)
    print("\t\tYour Transaction sleep")
    print("-" * 50)
    print("Your A/c xxxx123:")

    d2 = today.strftime("%d %B, %Y   Time: %H:%M:%S")
    print("Date:", d2)
    balenq()
