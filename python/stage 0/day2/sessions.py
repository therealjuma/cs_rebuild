def compute_active_time(events):
    sessions = {}
    totals = {}

    for ts, user, action in events:
        # checking first if the user has already login
        if action == "login":
            sessions[user] = ts

        elif action == "logout":
            total_time = ts - sessions[user]
            sessions[user] = total_time

        # Check how long the user has been on


    return totals

events = [
    (10, "alice", "login"),
    (20, "alice", "login"),     # invalidates previous
    (50, "alice", "logout"),    # counts from 20 → 50

    (15, "bob", "logout"),      # ignored
    (30, "bob", "login"),
    (75, "bob", "logout"),

    (40, "alice", "purchase"),  # irrelevant
]

session_one = compute_active_time(events)

print(session_one)