import string

#gigem{k3y63n_m3?_k3y63n_y0u!}
#jpZ2SaGCaahc5GN6
#j4Z2S09570095926

a = 'H'
flag = ""
index = 0
payload = "[OIonU2_<__nK<KsK"

for i in payload:
    for j in string.printable:
        data = (((ord(j)+12)*ord(a)+17) % 70 + 48)
        if ord(i) == data:
            flag += j
            a = i
            break

print (flag)


