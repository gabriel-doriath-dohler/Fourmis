import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from random import randrange, choice, random


def gen_fourmis(nb, taille):
    '''
    fourmis : liste des positions et des positions précédentes des fourmis
    grille[x][y] : vaut 1 ssi il y a une ou des fourmis en (x, y)
    grille_total[x][y] : nombre de fourmis qui sont passées en (x, y)
    '''
    positions = [(randrange(taille), randrange(taille)) for _ in range(nb)]
    grille = np.zeros((taille, taille), dtype=np.int64)
    grille_total = np.zeros((taille, taille), dtype=np.int64)
    fourmis = [(*pt, *pt) for pt in positions]

    for x, y, _, _ in fourmis:
        grille[x][y] = 1
        grille_total[x][y] += 1

    return fourmis, grille, grille_total


def argmax(cases, tab):
    val_max = -float('inf')
    xy_max = []
    for x, y in cases:
        if tab[x][y] == val_max:
            xy_max.append((x, y))
        elif tab[x][y] > val_max:
            val_max = tab[x][y]
            xy_max = [(x, y)]
    return xy_max


def argmin(cases, tab):
    val_min = float('inf')
    xy_min = []
    for x, y in cases:
        if tab[x][y] == val_min:
            xy_min.append((x, y))
        elif tab[x][y] < val_min:
            val_min = tab[x][y]
            xy_min = [(x, y)]
    return xy_min


def deplace(fourmis, grille, grille_total, p, evite):
    '''
    Déplace les fourmis celon les règles suivantes :
        - une fourmi ne peut pas monter.
        - une fourmi ne peut pas rester sur place.
        - une fourmi ne peut pas revenir sur sa position précédente.
        - avec une probabilité (1 - p) la fourmi ne fait pas attention au 2 dernières règles.
        - une fourmi va vers une case voisine où grille_total est maximal si evite est vrai.
        - une fourmi va vers une case voisine où grille_total est minimal si evite est faux.
    '''
    d = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]
    new_fourmis = []
    for x, y, x_old, y_old in fourmis:
        cases_voisines = list(filter(lambda pt: pt != (x_old, y_old), [((x + dx) % len(grille), (y + dy) % len(grille)) for dx, dy in d]))
        if random() < p:  # Suit toutes les règles.
            if evite:
                cases = argmax(cases_voisines, grille_total)
            else:  # Ne fait pas attention au 2 dernières règles.
                cases = argmin(cases_voisines, grille_total)
            x_new, y_new = choice(cases)
        else:
            x_new, y_new = choice(cases_voisines)
        new_fourmis.append((x_new, y_new, x, y))
    for x, y, x_old, y_old in new_fourmis:
        grille[x_old][y_old] = 0
        grille[x][y] = 1
        grille_total[x][y] += 1
    return new_fourmis


def simule(taille=10, nb_fourmis=10, nb_iter=100, p=0.8, evite=True):
    fourmis, grille, grille_total = gen_fourmis(nb_fourmis, taille)

    images = []
    images_total = []
    images.append(np.copy(grille))
    images_total.append(np.copy(grille_total))
    for i in range(nb_iter):
        images.append(np.copy(grille))
        images_total.append(np.copy(grille_total))
        fourmis = deplace(fourmis, grille, grille_total, p, evite)
    return np.array(images), np.array(images_total)


def save(images, images_total):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_axis_off()
    ax2.set_axis_off()
    ax1.set_title('Positions actuelles.')
    ax2.set_title('Positions cumulées.')

    im = ax1.imshow(images[0], vmin=0, vmax=np.max(images))
    im_total = ax2.imshow(images_total[0], vmin=0, vmax=np.max(images_total))
    def updatefig(j):
        im.set_array(images[j])
        im_total.set_array(images_total[j])
        return [im, im_total]

    ani = animation.FuncAnimation(fig, updatefig, frames=range(len(images)), interval=20, blit=True)
    ani.save('fourmis.mp4', dpi=300)


def main(taille, nb_fourmis, nb_iter, p, evite):
    images, images_total = simule(taille, nb_fourmis, nb_iter, p, evite)
    save(images, images_total)


if __name__ == '__main__':
    main(100, 200, 1000, 0.9, True)

