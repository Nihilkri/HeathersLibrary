from datetime import datetime
from typing import List
import AO3
import pandas as pd

print("Reading Login info...")
unpw = pd.read_csv(r"AO3.csv")
username, password = unpw['Username'][0], unpw['Password'][0]

print(f"{username} logging in...")
try:
  sess: AO3.Session = AO3.Session(username, password)
except AO3.utils.LoginError:
    print("Invalid username or password!")
except AO3.utils.InvalidIdError:
    print("Invalid login!")

print(f"Done! {username = }")
#print(f"{password = }")

print("Retrieving history...")
hist = sess.get_history(1, 0, 0, 60)
works: List[AO3.Work] = None
visits: int = 0
lastvisit: datetime = None
works, visits, lastvisit = zip(*hist)
work:AO3.Work = AO3.Work
titles = [work.title for work in works]
#authors = [work.authors for work in works]
#warnings = [work.warnings for work in works]
histdf = pd.DataFrame({"Title": titles,
                      #"Authors": authors,
                      #"Warnings": warnings,
                      "Visits": visits,
                      "Last visit": lastvisit})
AO3.Work

print(histdf)

# user: AO3.User = sess.user   #.User(username)
# print(f"{user.url = }")
# print(f"{user.bio = }")
# print(f"{user.works = }")  # Number of works published