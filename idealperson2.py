# idealperson.py
# pip install Pillow
from PIL import Image
import matplotlib.pyplot as plt
from random import choice

def create_candidates():
    candidates = {"1": {"picture":"images/1.jpg"}, 
                  "2": {"picture":"images/2.jpg"},
                  "3": {"picture":"images/3.jpg"},
                  "4": {"picture":"images/4.jpg"},
                  "5": {"picture":"images/5.jpg"},
                  "6": {"picture":"images/6.jpg"},
                  "7": {"picture":"images/7.jpg"},
                  "8": {"picture":"images/8.jpg"}}
    return candidates

def game(all, selectedlist):
    candidates = {k:all[k] for k in selectedlist}
    lst = candidates.keys()
    selected = []
    while len(lst) > 0:
        c1 = choice(lst)
        lst.remove(c1)
        c2 = choice(lst)
        lst.remove(c2)
        imgshow(c[c1]["picture"], c[c2]["picture"])
        plt.show()
        inputvalue = input("select 1 or 2: ")
        if inputvalue == 1:
            selected.append(c1)
        else:
            selected.append(c2)
    return selected

def imgshow(file1, file2):
    img1 = Image.open(file1)
    img2 = Image.open(file2)
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(img1)
    axes[1].imshow(img2)
    return plt

if __name__ == "__main__":
    c = create_candidates()
    semifinals = game(c, c.keys())
    print("semifinal candidates: ", semifinals)
    finals = game(c, semifinals)
    print("final candidates: ", finals)    
    winner = game(c, finals)
    print("winnder is: ", winner)

            
            
    