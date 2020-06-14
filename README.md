# Fourmis
Simulation de fourmis sur un tore. Tendance à prendre le même chemin ou à s'éviter.

grille_total[x][y] compte de nombre de fourmis qui sont passées par la case (x, y).
Les fourmis se déplacent selon les règles suivantes :
  - une fourmi ne peut pas monter.
  - une fourmi ne peut pas rester sur place.
  - une fourmi ne peut pas revenir sur sa position précédente.
  - avec une probabilité (1 - p) la fourmi ne fait pas attention au 2 dernières règles.
  - une fourmi va vers une case voisine où grille_total est maximal si evite est faux. (caractère attractif)
  - une fourmi va vers une case voisine où grille_total est minimal si evite est vrai. (caractère répulsif)
  
# Exemples
## Attractif : https://www.youtube.com/watch?v=UG4bMAezPVk
![alt text](https://github.com/gabriel-doriath-dohler/Fourmis/blob/master/attractif.png?raw=true)

## Répulsif : https://www.youtube.com/watch?v=PtZeTQ-D37
![alt text](https://github.com/gabriel-doriath-dohler/Fourmis/blob/master/repulsif.png?raw=true)
