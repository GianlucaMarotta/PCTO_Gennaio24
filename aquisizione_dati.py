from meanData import mean_data

while(True):
    angolo=float(input("quanto misura l'angolo: "))
    az, err_az=mean_data(log=False)

    with open("data.csv", "a+") as file:
        file.write(f"{angolo}\t{az[2]}\t{err_az[2]}\n")

