# 

Izsuperior = 0.25
Izinferior = 0.03
zinferior= -np.log(Izsuperior)/kNahuel
zsuperior = -np.log(Izinferior)/kNahuel

zbien  = np.arange(zinferior,zsuperior,0.2)
zmal =np.arange(zsuperior,zfRioArriba,0.2) 

Izbien = I0*np.e**(-kNahuel*zbien) 
Izmal = I0*np.e**(-kNahuel*zmal)
plt.fill_between(zbien, Izbien, color="green",label="Crecimiento bueno")

plt.fill_between(zmal, Izmal,color="red",label="Crecimiento malo")
plt.legend(loc="upper right")
plt.show()

