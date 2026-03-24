
def sum_list(c):
    total=0
    for i in c:
        total+=i
    return total

def average_list(c):
    return sum_list(c)/len(c)


def largest(c):
    largest=c[0]
    for i in c:
        if i>largest:
            largest=i
    return largest

def smallest(c):
    smallest=c[0]
    for i in c:
        if i<smallest:
            smallest=i
    return smallest


def duplicates(c):
    e=[]
    for i in range(len(c)):
        new=c[i]
        count=0
        for j in range(len(c)):
            if c[j] == new:
                count+=1
        already=False
        for k in range(i):
            if c[k] == new:
                already=True
        if not already and count>1:
            e.append(new)
    return e



def highest_frequency(c):
    max_count=0
    element=0
    for i in range(len(c)):
        x=c[i]
        count=0
        for j in range(len(c)):
            if c[j] == x:
                count+=1
        already=False
        for k in range(i):
            if c[k] == x:
                already=True
        if not already and count>max_count:
            max_count=count
            element=x
    return element



def main():
    c=[10,20,30,40,10,50,30,30]

    print("----------------------------------")
    print(f"Sum of List:",sum_list(c))
    print(f"Average of List:",average_list(c))
    print(f"Largest of List:",largest(c))
    print(f"Smallest of List:",smallest(c))
    print(f"Duplicates in List:",duplicates(c))
    print(f"Highest Frequency in List:",highest_frequency(c))
    print("----------------------------------")



main()
