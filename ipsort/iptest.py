iplist = ["1.1.1.1","192.168.1.110","10.192.2.4","10.50.2.3","10.50.2.10","111.120.12.1","172.18.5.112"]
ip_store=[]
ip_best=[]
def ip_split(ip):
    a,b,c,d=ip.split(".")
    a1=int(a) << 24
    b1=int(b) << 16
    c1=int(c) << 8
    d1=int(d)
    return a1+b1+c1+d1
def ip_restore(ip_s):
    a=ip_s>>24 &255
    b=ip_s >>16 &255
    c=ip_s >>8 &255
    d=ip_s &255
    return ".".join([str(a),str(b),str(c),str(d)])

for ip in iplist:
    ip_store.append(ip_split(ip))
ip_store.sort()
print(ip_store)
for ip in ip_store:
    ip_best.append(ip_restore(ip))
print(ip_best)