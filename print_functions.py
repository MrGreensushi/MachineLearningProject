import numpy as np
import matplotlib.pyplot as plt

#FUNZIONI PER LA STAMPA DI STATISTICHE SUL DB
def dataset_len(dataset):
  n = 0
  for i in range(len(dataset)):
    for j in range(len(dataset[i])):
      n = n + len(dataset[i][j])
  return n;

def immagini_nei_landmark(dataset):
  v = np.zeros(len(dataset))
  for i in range(len(dataset)):
    for j in range(len(dataset[i])):
      v[i] = v[i] + len(dataset[i][j])
  return v;

def valutazioni_landmarks(dataset):
  v = [ [0,0,0,0] for x in range(len(dataset))]
  for i in range(len(dataset)):
    for j in range(len(dataset[i])):
      v[i][j] = len(dataset[i][j])
  return v;

def good_ok_bad_junk(dataset):
  x = valutazioni_landmarks(dataset)
  v = [0,0,0,0]
  for i in range(len(x)):
    for j in range(len(x[i])):
      v[j] = v[j] + x[i][j]
  return v

def print_dataset_stats(dataset):
    print("Numero immagini del dataset: ", dataset_len(dataset))
    print("Numero di immagini nei vari landmark: ", immagini_nei_landmark(dataset))
    print("Immagini good-ok-bad-junk: ", good_ok_bad_junk(dataset))
    print("Per ogni landmark, quanti sono quelli good, ok, bad e junk:", valutazioni_landmarks(dataset))
    
#stampa esempi dato un generatore. Genera 25 foto a partire da un generatore e le visualizza
def print_data_aug(generatore):
    fig, axs = plt.subplots(nrows=5, ncols=5, figsize=(3,3))
    for i in range(5):
        for j in range(5):
            x = next(generatore)
            #print(x[1]) #label y se inserite in datagen.flow(x=...,y=...)
            #image = image[0][0]#.astype('uint8') #immagine se y inserite in datagen.flow(x=...,y=...)
            image = x[0]

            # plot image
            axs[i,j].imshow(image)
            axs[i,j].axis('off')
    return

#stampa le 3 foto di un array tripletta
def stampa_tripletta(tripletta):
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(10,10))
    for i in range(0,3):
        img = tripletta[i]
        axs[i].imshow(img.numpy())
        axs[i].axis('off')
    return

#stampa tutte le immagini di una certa classe
def print_class_good_images(dataset, classe):
    fig, axs = plt.subplots(nrows=len(dataset[classe][1]), ncols=1, figsize=(150,150))
    for i in range(0,len(dataset[classe][1])):
        img = dataset[classe][1][i]
        axs[i].imshow(img)
        axs[i].axis('off')
    return