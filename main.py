import random
def gen(aaa):
    cope = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    con = "".join(random.choice(cope) for i in range(aaa))5
    print("la clave generada es", con)
    return con
aa = int(input("longitud de la contraseña?:"))
test = gen (aa)
