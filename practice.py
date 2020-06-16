clientDict = [{'sid': '8c99df5b386d46b8a8ea34adb25a634c', 'userName': 'unknown'}, {'sid': 'e62dbdd4450a4370b180bf93a90814a4', 'userName': 'unknown'}, {
    'sid': 'b5a3081f174d4c54a58300c9d87f0b50', 'userName': 'unknown'}, {'sid': '605d7609bf774b488e7cde427db0253b', 'userName': 'unknown'}]

sidTemp = 'b5a3081f174d4c54a58300c9d87f0b50'
print(clientDict)

# for x in clientDict:
#     if sidTemp == x["sid"]:
#         clientDict.remove(x)

# print(clientDict)
userName= 'abidzaidi'

for x in clientDict:
    if sidTemp == x["sid"]:
        x["userName"] = userName
        break

print(clientDict)
