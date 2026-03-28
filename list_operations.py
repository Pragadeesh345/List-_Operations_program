
def sum_list(c):
    total=0
    for i in c:
        total+=i
    return total

def average_list(c):
    t=0  # repeating sum of list process so it doesn't crash when choice = 2 without calculating sum of list first
    for i in c:
        t+=i
    average=t/len(c)
    return average


def largest_list(c):
    largest=c[0]
    for i in c:
        if i>largest:
            largest=i
    return largest

def smallest_list(c):
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
    print("Enter values with spaces for list")
    print("Example: 1 2 3 4")
    c=list(map(int,input("Enter the Values for list:").split()))
    while True:
            print("----------------------------------")
            print("1 Sum of List")
            print("2 Average of List")
            print("3 Largest of List")
            print("4 Smallest of List")
            print("5 Duplicates in List")
            print("6 Highest Frequency in List")
            print("0 Exit")
            print("----------------------------------")

            x=int(input("Enter your choice:"))

            if x == 1:
                total=sum_list(c)
                print("Sum of list:",total)
            elif x == 2:
                average=average_list(c)
                print("Average of list:",average)
            elif x == 3:
                largest=largest_list(c)
                print("Largest in List:",largest)
            elif x == 4:
                smallest=smallest_list(c)
                print("Smallest in list:",smallest)
            elif x == 5:
                e=duplicates(c)
                print("Duplicates in List:",e)
            elif x == 6:
                element=highest_frequency(c)
                print("Highest Frequent element in list:",element)
            elif x == 0:
                print("Exiting...")
                break

main()
