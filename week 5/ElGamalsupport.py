from Crypto.PublicKey import ElGamal

def export_EGkey(key,keytype):
    if keytype == 0: #private key
        file_out = open("ElGamalprivate", "w")
    if keytype == 1: #public key
        file_out = open("ElGamalpublic", "w")

    file_out.write(str(key))
    file_out.close()

def export_EGparam(param,paramtype):
    if paramtype == 0: #group order prime
        file_out = open("ElGamalprime", "w")
    if paramtype == 1: #group generator
        file_out = open("ElGamalg", "w")

    file_out.write(str(param))
    file_out.close()


def ElGamal_keygen():
    key = ElGamal.generate(bits=256,randfunc=None)
    private_key = key.x
    public_key = key.y
    p = key.p
    g = key.g
    #private_key = 41231302884341847366193981764998709588660948018987339808971609484986791000890
    #public_key = 60045148663949004016326603904631434432115715630389036364538190632668085776991
    
    #print(private_key, public_key, g, p)
    export_EGkey(private_key, 0)
    export_EGkey(public_key, 1)
    export_EGparam(p, 0)
    export_EGparam(g, 1)


def ElGamal_param_load():
    pkey = int(open("ElGamalpublic").read())
    skey = int(open("ElGamalprivate").read())
    p = int(open("ElGamalprime").read())
    g = int(open("ElGamalg").read())
    return skey, pkey, p, g