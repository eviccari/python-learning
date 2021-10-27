browsing_sessions = []
browsing_sessions.append(1)
browsing_sessions.append(2)
browsing_sessions.append(3)

print(browsing_sessions)
last = browsing_sessions.pop()
last = browsing_sessions.pop()
last = browsing_sessions.pop()

print(last)
print(browsing_sessions)

if not browsing_sessions:
    print("The stack is empty")
