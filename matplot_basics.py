import matplotlib.pyplot as plt

# x = [1,2,3,4]
# y = [10,20,25,30]

# plt.plot(x, y)

# plt.title("Simple Line Chart")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")

# plt.show()


names = ["Ravi","Aman","Neha"]
marks = [80,70,90]

plt.bar(names, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()


age = [22,25,30,35,40]
salary = [20000,30000,50000,70000,90000]

plt.scatter(age, salary)

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()


data = np.random.randint(1,100,50)

plt.hist(data)

plt.title("Distribution of Numbers")

plt.show()


x = [1,2,3,4]

y1 = [10,20,30,40]
y2 = [5,15,25,35]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

plt.legend()

plt.show()


data = {
    "age":[22,25,30,35],
    "salary":[20000,30000,50000,70000]
}

df = pd.DataFrame(data)

plt.scatter(df["age"], df["salary"])

plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()