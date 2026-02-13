import matplotlib.pyplot as plt


projects = [
    {"name":"AI dashboard", "status": "Completed", "year": 2022},
    {"name": "IOT", "status": "com", "year": 2022},
    {"name": "Web app", "status": "Sold", "year": 2022},
]




projects = ["AI dashboard", "IOT", "Web app"]
completion_dates = [1, 2, 3]

plt.plot(completion_dates, projects)
plt.xlabel("Timeline(2022)")
plt.ylabel("Projects")
plt.title("Completed projects")
plt.show()



