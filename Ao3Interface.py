import AO3
import pandas as pd

print("Reading Login info...")
unpw = pd.read_csv(r"C:\Users\Nihil\Documents\AO3.csv")
username, password = unpw['Username'][0], unpw['Password'][0]

print(f"{username} logging in...")
try:
  sess: AO3.Session = AO3.Session(username, password)
except AO3.utils.LoginError:
    print("Invalid username or password!")

print(f"Done! {username = }")
#print(f"{password = }")

print("Retrieving history...")
#hist = sess.get_history(1, 0, 0, 60)
#hist = sess.get_subscriptions(True)

#print(hist)

# user: AO3.User = sess.user   #.User(username)
# print(f"{user.url = }")
# print(f"{user.bio = }")
# print(f"{user.works = }")  # Number of works published