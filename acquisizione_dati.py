from meanData import mean_data

while(True):
    teta = float(input("misura angolo: "))
    dato, err = (mean_data(log=False))
    print(dato[2], err[2])
    with open("dato.csv", "a+") as file:
        file.write(f"{teta}\t {dato[2]}\t {err[2]}\n" )
    

