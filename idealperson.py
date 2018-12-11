# idealperson.py
# pip install Pillow
from PIL import Image
import matplotlib.pyplot as plt

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

def semifinal(all, selectedlist):
    candidates = {k:all[k] for k in selectedlist}
    return candidates

def imgshow(file1, file2):
    img1 = Image.open(file1)
    img2 = Image.open(file2)
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(img1)
    axes[1].imshow(img2)
    return plt

if __name__ == "__main__":
    c = create_candidates()
    lst = c.keys()
    imgshow(c[lst[0]]["picture"], c[lst[0]]["picture"])
    plt.show()
    selected = []
    for l in lst:
        value = input("select 0 or 1")
        selected.append(value)
    print(selected)









    
