def ip_to_int(ip):
  a, b, c, d = ip.split(".")
  return (int(a) << 24) + (int(b) << 16) + (int(c) << 8) + int(d)

#首先，将每个部分转换为整数，例如，如果IP地址是"1.1.1.1"，那么a=1, b=1, c=1, d=1。
#然后，将每个部分按照其在IP地址中的位置进行位移运算，即将a左移24位，将b左移16位，将c左移8位，将d不变。这样，每个部分占据了整数的一个字节（8位），例如，如果a=1, b=1, c=1, d=1，那么位移后的结果是：
#a << 24 = 00000001 00000000 00000000 00000000
#b << 16 = 00000000 00000001 00000000 00000000
#c << 8 = 00000000 00000000 00000001 00000000
#d = 00000000 00000000 00000000 00000001
#最后，将这四个部分进行加法运算，得到一个整数，例如，如果a=1, b=1, c=1, d=1，那么加法后的结果是：
#(a << 24) + (b << 16) + (c << 8) + d = 16843009 这样，就可以将IP地址转换为一个整数，方便进行排序和比较。
def int_to_ip(n):
  a = (n >> 24) & 255
  b = (n >> 16) & 255
  c = (n >> 8) & 255
  d = n & 255
  return ".".join([str(a), str(b), str(c), str(d)])
# join前面的“.”是指定连接符

# 定义一个列表，存储给定的IP地址
iplist = ["1.1.1.1","192.168.1.110","10.192.2.4","10.50.2.3","10.50.2.10","111.120.12.1","172.18.5.112"]

# 创建一个空列表，存储转换后的整数
intlist = []

# 遍历给定的IP地址列表，将每个IP地址转换为整数，并添加到整数列表中
for ip in iplist:
  intlist.append(ip_to_int(ip))

print(intlist)
# # 对整数列表进行排序
# intlist.sort()
#
# # 创建一个空列表，存储排序后的IP地址
# sorted_iplist = []
#
# # 遍历排序后的整数列表，将每个整数转换为IP地址，并添加到IP地址列表中
# for n in intlist:
#   sorted_iplist.append(int_to_ip(n))
#
# # 输出排序后的IP地址列表
# print(sorted_iplist)