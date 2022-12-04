d = {"George":24,
     "Tom":32}

# or
# d = dict()

# or
d = {}
d["George"] = 24
d["Tom"] = 32
d["Jenny"] = 16

print(d)
print(d["George"])
print(d["Jenny"])

d["Jenny"] = 20
print(d["Jenny"])

for key, value in d.items():
    print("key:", key)
    print("value:", value)


