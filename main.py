# Invertir una cadena

from asyncore import file_dispatcher

from pip import main


palabra = "Hola"
cadena = []

x = len(palabra)
print(x)
while x > 0:
    x -= 1
    cadena.append(palabra[x])

print(cadena)
    
# git clone <repositorio>   -> Clonar todo el repositorio
# git fetch                 -> Una vez clonado, descarga la informacion
# git pull origin main      -> Me trae el ultimo commit
# git commit -am "mensaje"  -> Guardar mis cambios locales
# git push origin main      -> Para empujar al servidor

#git checkout <nombre rama>     -> Cambio de rama
#git branch <nombre rama>       -> Crea una nueva rama
#git checkout -B <nombre rama>  -> Crea una nueva rama y se mueve hacia ella


#git reset --hard  -> Te mueve al ultimo commit hecho, quita todos los cambios que no se han commiteado.mueve el head al ultimo cambio hecho.  Head es donde estoy parado. (puntero -> Apunta al estado actual)

#git checkout HEAD <nombre archivo> -> De esta forma puedo deshacer los cambios solo de un archivo y no de todo el repo.

#git log  -> permite ver la historia de los commit
#git log --oneline  -> permite ver la historia del commit de forma resumida
#git log --oneline --graph  -> historia de forma un poco mas grafica

#git checkout <nombre commit>   -> Puedo volver a un commit anterior
#git switch -                   -> me devuelve los cambios