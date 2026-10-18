import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("PolarizationLab")
st.write("Interface TE / TM – première version")

# Interface utilisateur
st.title("Module 1 : Plan d'interface")
n1 = st.number_input("Indice du milieu 1 (n1)", value=1.0) #n1
n2 = st.number_input("Indice du milieu 2 (n2)", value=1.5) #n2
theta_deg = st.number_input("Angle d'incidence θ (°)", value=30.0) #theta incident
wavelenght = st.number_input("Longueur d'onde λ (nm)") #lambda
polarization = st.radio("Polarisation", ["TE", "TM"])

theta_i = np.radians(theta_deg) #conversion en radians
#Calcul Snell
theta_t = np.arcsin(n1/n2 * np.sin(theta_i))

#Graphe
L=0.8
fig, ax = plt.subplots(figsize=(6,6))
ax.plot([-1,1],[0,0], 'k', linewidth=2)
#rayon incident
x_inc = [-L*np.sin(theta_i),0]
y_inc = [L*np.cos(theta_i),0]
ax.plot(x_inc, y_inc, color='blue', linewidth=2, label='Incident')

ax.annotate(
    "",
    xy=(0, 0),
    xytext=(-0.15*np.sin(theta_i), 0.15*np.cos(theta_i)),
    arrowprops=dict(arrowstyle="->", color='blue', lw=2)
)

#rayon réfléchie
x_ref = [0, L*np.sin(theta_i)]
y_ref = [0, L*np.cos(theta_i)]
ax.plot(x_ref, y_ref, color='red', linewidth=2, label='Réfléchi')

ax.annotate(
    "",
    xy=(0.15*np.sin(theta_i), 0.15*np.cos(theta_i)),
    xytext=(0,0),
    arrowprops=dict(arrowstyle="->", color='red', lw=2)
)

#rayon transmis
x_trans = [0, L*np.sin(theta_t)]
y_trans = [0, -L*np.cos(theta_t)]
ax.plot(x_trans, y_trans, color='green', linewidth=2, label='Transmis')

ax.annotate(
    "",
    xy=(0.15*np.sin(theta_t), -0.15*np.cos(theta_t)),
    xytext=(0, 0),
    arrowprops=dict(arrowstyle="->", color='green', lw=2)
)

#mise en forme
ax.set_aspect('equal')
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.set_title("Reflexion et transmission à une interface plane")
plt.show()
st.pyplot(plt)

#Coef de Fresnel
if polarization == "TE":
    r = (n1 * np.cos(theta_i) - n2 * np.cos(theta_t))/(n1 * np.cos(theta_i) + n2 * np.cos(theta_t))
    t = 2*n1*np.cos(theta_i)/(n1*np.cos(theta_i) + n2*np.cos(theta_t))

elif polarization == "TM":
    r = (n1*np.cos(theta_t) - n2*np.cos(theta_i))/(n1*np.cos(theta_t) + n2*np.cos(theta_i))
    t = 2*n1*np.cos(theta_i)/(n1*np.cos(theta_t) + n2*np.cos(theta_i))

R = np.abs(r)**2
T = np.abs(t)**2 * (n2 * np.cos(theta_t))/(n1 * np.cos(theta_i))
sum_RT = R + T
phi = np.angle(r)


#Angle de Brewster
theta_B = np.arctan(n2/n1) if polarization == "TM" else None

#Affichage
st.write(f"Coefficient de réflexion R : {R:.3f}")
st.write(f"Coefficient de transmission T : {T:.3f}")
st.write(f"Vérification R + T = {sum_RT:.3f} ")
if theta_B:
    st.write(f"Angle de Brewster θ_B = {theta_B:.2f} radians ou θ_B = {np.degrees(theta_B):.2f}°")
st.write (f"Phase réfléchie : {np.degrees(phi):.2f}°")

#Graphique des champs
x= np.linspace(0,2*np.pi, 500)
E_inc = np.cos(x)
E_ref = r* np.cos(x)
E_trans = t*np.cos(x)

plt.figure(figsize=(8,4))
plt.plot(x, E_inc, label="Incident")
plt.plot(x, E_ref, label="Réfléchi")
plt.plot(x, E_trans, label="Transmis")
plt.legend()
plt.xlabel("x")
plt.ylabel("Amplitude")
st.pyplot(plt)

















