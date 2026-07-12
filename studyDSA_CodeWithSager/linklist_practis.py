""" class emptyLinkListBanana:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        # aaab yaha ek khali link list creat ho gyi


class linklistKeDibboKoJodna:
    def __init__(self, linklist=None):
        self.linklist = linklist

    def insertinEnd(self, data):
        # self.node = node
        self.data = data
        emptyLinkListBanana(data)


ll = emptyLinkListBanana()
# ll2 = emptyLinkListBanana("Apple")

# ll.next = ll2
ll.data = "njmnkmnkmn"
print() """







""" 
class khaliNode :
    def __init__(self,data,next=None):
        self.data = data
        self.next = next  #ek node banaliya jo user se data + next node ka adress lega

class linklist4Public:

    if data is None :
     def __init__(self, nodedata):
        nayiLinkList = khaliNode(nodedata) # user se data lega or ek node bana dega 

    def printlinklist(self):
        print(nayiLinkList)
                        
# === aasli use shuru ===
mylist = linklist4Public("Apple")
mylist.printlinklist()
print(mylist.printlinklist()) """

class khaliNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next  # Ek node ban gaya jo data aur agle node ka pata rakhega

class linklist4Public:
    def __init__(self, nodedata=None):
        # Agar user ne data diya hai (None nahi hai)
        if nodedata is not None:
            # Humne manager ke magic bag (self) me pehla dibba daal diya
            self.head_node = khaliNode(nodedata) 
        else:
            self.head_node = None

    def printlinklist(self):
        # Manager se bola ki apne bag se nikal kar pehle dibbe ka data dikhao
        if self.head_node is not None:
            print(self.head_node.data)
        else:
            print("Train khali hai!")

                
# === asli use shuru ===
# 1. Humne mylist banayi aur usme "Apple" daal diya
mylist = linklist4Public("Apple")

# 2. Ab humne printlinklist function ko call kiya (bina bahar print lagaye)
mylist.printlinklist()












































""" 
# 1. Ye hamara dibba banane wala factory hai
class emptyLinkListBanana:
    def __init__(self, data, next=None):
        self.data = data    # Dibbe ke andar ka saaman
        self.next = next    # Agle dibbe ka address (hook)

# 2. Ye hamara dibbo ko jodne wala manager hai
class linklistKeDibboKoJodna:
    def __init__(self):
        self.head = None    # Shuru me humare paas ek bhi dibba nahi hai (Train khali hai)

    def insertinEnd(self, saaman):
        # STEP A: Pehle hawa me dibba banane ki jagah, use ek naam do (naya_dibba)
        naya_dibba = emptyLinkListBanana(saaman)

        # STEP B: Agar train me abhi tak koi dibba nahi hai, toh isi ko pehla dibba bana do
        if self.head is None:
            self.head = naya_dibba
            return

        # STEP C: Agar pehle se dibbe hain, toh engine se shuru karo aur aakhiri dibbe tak jao
        aakhiri = self.head
        while aakhiri.next is not None:
            aakhiri = aakhiri.next

        # STEP D: Aakhiri dibbe ke hook (.next) par naye dibbe ko baandh (tie) do!
        aakhiri.next = naya_dibba


# --- AB CHALA KAR DEKHTE HAIN ---

# 1. Ek khali list (manager) banayi
manager = linklistKeDibboKoJodna()

# 2. Manager ko bola dibbe jodo
manager.insertinEnd("Mango")   # Ye pehla dibba ban gaya
manager.insertinEnd("Apple")   # Ye Mango ke peeche jud gaya
manager.insertinEnd("Banana")  # Ye Apple ke peeche jud gaya

# 3. Check karte hain ki kya Mango ke peeche Apple juda?
print("Pehla Dibba:", manager.head.data)        # Output: Mango
print("Doosra Dibba:", manager.head.next.data)  # Output: Apple
print("Teesra Dibba:", manager.head.next.next.data) # Output: Banana """