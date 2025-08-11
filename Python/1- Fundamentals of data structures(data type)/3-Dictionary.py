# key-value
# Dictionary={key:value, key:value, key:value}

nomre={"riazi":10, "programming":15, "motoon":2}
print(nomre["riazi"])   #10

nomrat={
    "bita": {
        "riazi":12,
        "programming":18,
        "motoon":11
    },
    "sara": {
        "riazi":15,
        "programming":16,
        "motoon":19
    }
}
print(nomrat["bita"])           # {'riazi': 12, 'programming': 18, 'motoon': 11}
print(nomrat["sara"]["riazi"])  # 15


# have methods with .
print(nomre.values())   # [10, 15, 2]
print(nomre.keys())     # ['riazi', 'programming', 'motoon']
print(nomrat.values())  # [{'riazi': 12, 'programming': 18, 'motoon': 11}, {'riazi': 15, 'programming': 16, 'motoon': 19}]
print(nomre.items())    # [('riazi', 10), ('programming', 15), ('motoon', 2)]

#  .get  function
price ={"apple":100, "banana":150, "orange":85}
print(price["apple"])       # 100
print(price.get("apple"))   # 100
#print(price["peach"])       # error
print(price.get("peach"))   # none      return nothing(without error)

print(price.get("peach", -1))   # -1    if peach exist, return "peach", Otherwise return -1
print(price.get("apple", -1))

# nested dic (imbricat - تو در تو)
numbers ={"list1":[1, 2, 3, 4], "list2":[5, 3, 1, 3]}
print(numbers["list1"])         # [1, 2, 3, 4]
print(numbers["list1"][2])      # 3
print(numbers["list1"][2] * 5)  # 15

classes ={1:["sara", "mohammad", "mitra"], 2: ["anca", "joe", "mara"]}
print(classes[2])       # ['anca', 'joe', 'mara']
print(classes[2][1])    # joe
print(classes[2][-1])   # mara
print(classes[2][2].upper())    # MARA
print(classes[2][2].upper()[2]) # R

# add to dictionary
classes[3] = ["shiva", "leila", "nazi"]
print(classes)  # {1: ['sara', 'mohammad', 'mitra'], 2: ['anca', 'joe', 'mara'], 3: ['shiva', 'leila', 'nazi']}
# change and delete
fruit_price = {"apple": 1500, "banana": 1000, "orange": 1200}
fruit_price["banana"]=1100          #  {"apple": 1500, "banana": 1100, "orange": 1200}
fruit_price.__delitem__("apple")    #  {"banana": 1100, "orange": 1200}
print(fruit_price)