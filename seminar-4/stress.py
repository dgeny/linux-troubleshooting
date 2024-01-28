from hashlib import sha384


def hard():
    hash384 = sha384('password'.encode())
    c=0
    while c < 50000:
        hash384.update(hash384.digest())
        c = c+1 
    return { "status": 1, "message": hash384.hexdigest() }  


if __name__ == "__main__":
    print(hard())
 