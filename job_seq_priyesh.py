#data model for the job sequencing problem- python program

from audioop import reverse


Job = (input("enter the job value: "))
Job = Job.split()
Job = [(x) for x in Job]

Profit = (input("enter the profit value: "))
Profit = Profit.split()
Profit = [int(y) for y in Profit]

deadline = (input("enter the deadline value: "))
deadline = deadline.split()
deadline = [int(z) for z in deadline]
#print(Job,Profit,deadline)

sorted_array = [(Job[i], Profit[i], deadline[i]) for i in range(0,len(Profit))]
#print(sorted_array)
max_deadline = sorted(sorted_array, key=lambda i: i[2],reverse=True)
n = max_deadline[0][2]
#print(max_deadline)
arr = sorted(sorted_array, key=lambda i: i[2], reverse=True)

def job_seq(max_deadline,arr):
    j_exe = []
    for i in range(max_deadline):
        max_item = arr[0]
        for item in arr:
            if item[2] == i+1: #multiple jobs with same deadline
                if item[1] > max_item[1]:
                    max_item = item

        j_exe.append(max_item)
    return j_exe
print(job_seq(n,arr))

