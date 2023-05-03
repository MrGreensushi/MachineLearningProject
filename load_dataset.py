import os
from PIL import Image
import numpy as np
import random

user = [''];

class_names = ['paris_defense', 'paris_eiffel', 'paris_invalides', 'paris_louvre', 'paris_moulinrouge', 'paris_museedorsay', 'paris_notredame', 'paris_pantheon', 'paris_pompidou', 'paris_sacrecoeur', 'paris_triomphe' ]

good = set();
ok = set();
bad = set();
junk = set();

dataset = [ [[],[],[],[]] for x in range(len(class_names))]

def set_user(x):
    user[0] = x
    return

def get_dirs():
    if(user[0]=="Daniele"):
        groundtruth_dir = r"C:\Users\dansp\OneDrive\Desktop\gdz"
        dataset_dir = r"C:\Users\dansp\OneDrive\Desktop\paris"
    elif(user[0]=="Andrea"):
        groundtruth_dir = r"D:\Andrea\Downloads\gzp"
        dataset_dir = r"D:\Andrea\Downloads\Paris120x120"
    else:
        groundtruth_dir = r"null"
        dataset_dir = r"null"
    print("groundtruth_dir: ", groundtruth_dir, "\ndataset_dir: ", dataset_dir)
    return groundtruth_dir, dataset_dir

def get_dataset(groundtruth_dir, dataset_dir, class_names):
    leggi_ground_truth_files(groundtruth_dir)
    print("Numero di good: ", len(good))
    print("Numero di ok: ", len(ok))
    print("Numero di bad: ", len(bad))
    print("Numero di junk: ", len(junk))

    carica_dataset_da_directory(dataset_dir, class_names)
    return dataset

def get_classnames():
    return class_names;
    
#Itera i file txt nella directory
def leggi_ground_truth_files(directory):
  for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
      rank = filename.split("_")[-1] #la parte finale del nome del file
      if rank == "good.txt":
        leggi_file(f,good)
      elif rank == "ok.txt":
        leggi_file(f,ok)   
      elif rank == "bad.txt":
        leggi_file(f,bad)
      elif rank == "junk.txt":
        leggi_file(f,junk)
      #elif rank == "query.txt":
        #leggi_file(f,query)
  return;


def leggi_file(f, s):
  with open(f) as f:
    lines = f.readlines()
    for line in lines:
      #rimuovo il \n finale e aggiungo .jpg
      line = line[:len(line)-1] + ".jpg"
      s.add(line)
  return;

#Carica il dataset scartando le foto che non hanno una valutazione o ne hanno
#più di una
def carica_dataset_da_directory(dataset_dir, class_names):
  #cicla nelle entry della directory
  for filename in os.listdir(dataset_dir):
    f = os.path.join(dataset_dir, filename)
    # checking if it is a file
    if os.path.isfile(f):
      valutazione = carica_valutazione(filename);
      label = carica_label(filename, class_names)
      carica_foto(f, dataset, valutazione, label)
  return;


def carica_foto(f, dataset, valutazione, label):
  if label == -1 or valutazione < 0:
    return #foto senza valutazione o senza label, scartata

  img = Image.open(f)
  pix = np.array(img)/255
  if(pix.shape != (120,120,3)): #check sulle dimensioni dell'immagine
    return
  dataset[label][valutazione].append(pix)
  return;


def carica_label(filename, class_names):
  for i in range(len(class_names)):
    if(filename.startswith(class_names[i])):
      return i
  return -1


def carica_valutazione(filename):
  flag = 0
  x = [0,0,0,0] #flag per presenza di filename in good, ok, bad e junk
  if filename in good:
    x[0]=1
  if filename in ok:
    x[1]=1
  if filename in bad:
    x[2]=1
  if filename in junk:
    x[3]=1

  if sum(x) > 1:
    #print(filename, ": valutazioni discordanti")
    return -1
  if sum(x) == 0:
    #print(filename, ": valutazione non disponibile")
    return -2

  for i in range(4):
    if x[i] == 1:
      return i #0:good, 1:ok, 2:bad, 3:junk
  return 0;

def shuffle(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            random.shuffle(data[i][j])
    return
    