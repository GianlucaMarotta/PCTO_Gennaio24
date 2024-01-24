from meanData import mean_data

theta = input("Che angolo?")
print(theta)

a_z, err_a_z = mean_data(log=False)
with open("data.csv", "a+") as file:
    file.write(f"{theta}\t{a_z[2]}\t{err_a_z[2]}\n")
