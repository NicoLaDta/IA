import numpy as np

x_entrer = np.array(([3,1.5],[2, 1],[4,1.5],[3,1],[3.5,0.5],[2,0.5],[5.5,1],[1,1],[4,1.5]),dtype=float)
y = np.array(([1],[0],[1],[0],[1],[0]),dtype=float) # Données de sortie 1 = Rouge / 0 = Bleu

x_entrer = x_entrer/np.amax(x_entrer, axis=0)

X = np.split(x_entrer,[8])[0]
xPrediction = np.split(x_entrer,[8])[1]

print(xPrediction)

