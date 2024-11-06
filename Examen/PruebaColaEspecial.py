import ColaEspecial

max=10

col = ColaEspecial.ColaEspecial(max)

col.insert("l")
col.insert("m")
col.insert("q")
col.insert("o")
col.insert("p")
col.insert("h")
col.insert("c")
col.insert("r")
col.insert("e")
col.insert("v")

col.mostrar()

col.insert("A")
col.insert("B")
col.insert("C")
col.insert("D")
col.insert("E")
col.insert("F")
col.insert("G")
col.insert("H")
col.insert("I")
col.insert("J")

for i in range(col.__len__,0,-1):
    if i > 10:
        for j in range(i):
            col.delete(col.get(9))
            col.insert(j)


