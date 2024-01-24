from meanData import mean_data

angolo=int(input("Inserisci angolo:"))
mean,std=mean_data()
a_z=mean[2]
f=open("data_Z","a+")
f.write(f"{angolo} \t {a_z} \t {std[2]} \n")
f.close()