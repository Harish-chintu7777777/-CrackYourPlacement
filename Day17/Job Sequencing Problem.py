Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Job:
...     def __init__(self, id, deadline, profit):
...         self.id = id
...         self.deadline = deadline
...         self.profit = profit
... 
... class Solution:
...     def JobScheduling(self, jobs, n):
...         jobs = sorted(jobs, key=lambda x: x.profit, reverse=True)
...         
...         max_deadline = max(job.deadline for job in jobs)
...         
...         timeline = [-1] * (max_deadline + 1)
...         
...         count_jobs = 0
...         total_profit = 0
...         
...         for job in jobs:
...             for t in range(job.deadline, 0, -1):
...                 if timeline[t] == -1:
...                     timeline[t] = job.id
...                     count_jobs += 1
...                     total_profit += job.profit
...                     break
...         
