mapa = [[2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,0,1,1,3,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2]]
fila= 3
columna= 3
while True:
    for x in (mapa):
        for y in x:
            print y,
        print
    movimiento =str(raw_input(" Hacia donde te quieres mover\n a - izquierda\n d - derecha\n w - arriba\n s - abajo\n q - salir:"))    
    if movimiento == "d":
        if mapa [fila][columna + 1]==1:
            columna = columna + 1
            mapa [fila][columna]=0 
            mapa [fila][columna - 1]=1 

    if movimiento == "a":
        if mapa [fila][columna - 1]==1:
            columna = columna - 1
            mapa [fila][columna]=0 
            mapa [fila][columna + 1]=1 

    if movimiento == "w":
        if mapa [fila - 1][columna]==1:
            fila= fila - 1
            mapa [fila][columna]=0
            mapa [fila + 1][columna]=1

    if movimiento == "s":
        if mapa [fila + 1][columna]==1:
            fila= fila + 1
            mapa [fila][columna]=0
            mapa [fila - 1][columna]=1

    if movimiento == "d":
         if mapa [fila][columna + 1]==3 and mapa [fila][columna + 2]==1:
                mapa [fila][columna + 1]=0
                mapa [fila][columna + 2]=3
                mapa [fila][columna]=1
                columna=columna+1

    if movimiento == "a":
         if mapa [fila][columna - 1]==3 and mapa [fila][columna - 2]==1:
                mapa [fila][columna - 1]=0
                mapa [fila][columna - 2]=3
                mapa [fila][columna]=1
                columna=columna-1

    if movimiento == "s":
         if mapa [fila + 1][columna]==3 and mapa [fila + 2][columna]==1:
                mapa [fila + 1][columna]=0
                mapa [fila + 2][columna]=3
                mapa [fila][columna]=1
                fila=fila + 1

    if movimiento == "w":
         if mapa [fila - 1][columna]==3 and mapa [fila - 2][columna]==1:
                mapa [fila - 1][columna]=0
                mapa [fila - 2][columna]=3
                mapa [fila][columna]=1
                fila=fila - 1

    if movimiento == "f":
            if mapa[fila][columna + 1]==3:
                 if mapa [fila][columna + 2]==3:
                       if  mapa [fila][columna + 3]==1:
                                 mapa [fila][columna]=1
                                 mapa [fila][columna + 1]=0
                                 mapa [fila][columna + 2]=3
                                 mapa [fila][columna + 3]= 3
                                 columna=columna + 1
    if movimiento == "f":
            if mapa[fila][columna - 1]==3:
                if mapa [fila][columna - 2]==3:
                      if  mapa [fila][columna - 3]==1:
                                 mapa [fila][columna]=1
                                 mapa [fila][columna - 1]=0
                                 mapa [fila][columna - 2]=3
                                 mapa [fila][columna - 3]= 3
                                 columna=columna-1
    if movimiento == "f":
            if mapa[fila - 1][columna]==3:
                if mapa [fila - 2][columna]==3:
                       if  mapa [fila - 3][columna]==1:
                                 mapa [fila][columna]=1
                                 mapa [fila - 1][columna]=0
                                 mapa [fila - 2][columna]=3
                                 mapa [fila - 3][columna]= 3
                                 fila=fila - 1

    if movimiento == "f":
            if mapa[fila + 1][columna]==3: 
                if mapa [fila + 2][columna]==3:
                       if  mapa [fila + 3][columna]==1:
                                 mapa [fila][columna]=1
                                 mapa [fila + 1][columna]=0
                                 mapa [fila + 2][columna]=3
                                 mapa [fila + 3][columna]= 3
                                 fila=fila + 1



    elif movimiento == 'q':
        break