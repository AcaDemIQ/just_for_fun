from functools import reduce

lst = [15,1,25,2,30,3,10,5]

lst = zip(lst[1::2], lst[0::2]) # приводим в удобный вид через кортежи (время, скорость)

step = lambda c, p: (p[0], c[1] + (p[0] - c[0])*p[1]) # (новое_время, общее_расстояние)

print(reduce(step, lst, initial=(0,0))[1]) # основной алгоритм



