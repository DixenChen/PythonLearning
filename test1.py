#This is to learn mutable, immutable objects
#mutable data type: list, disctionary, set
#immutable data type: int, string, float, tuple(unchangable)
def processList(mList):
    mList[0]=9
    mList.append(5)

def processDictionary(mDic):
    mDic["city"] = "Parkland"
    mDic["name"] = "Ling"
    
def processString(str):
    str = "Dixen"

def processInt(num:int):
    num = 11

def processTuple(mTup):
    mTup=(7,8,9)

m_list = [1,2,3]
processList(m_list)
print("mutable object type-list")
for item in m_list:
    print(item)

m_dict = {"name":"Dixen", "age":50}
processDictionary(m_dict)
for key, value in m_dict.items():
    print(f"Key: {key}, Value: {value}")

mStr = "Yuxi"
processString(mStr)
print("immutable object type-string")
print(mStr)

mInt = 9
processInt(mInt)
print("immutable object type-int")
print(mInt)

m_Tup=(1,2,3)
processTuple(m_Tup)
print("immutable object type-tuple")
for item in m_Tup:
    print(item)


