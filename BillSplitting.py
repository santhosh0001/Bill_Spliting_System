class User:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.toReceive={}
        self.toPay={}
    
    def splitEqual(self,amount,mainUser,sharingPersonsList):
        individualAmount=amount//(len(sharingPersonsList)+1)
        for user in sharingPersonsList:
            if mainUser.name in user.toPay:
                user.toPay[mainUser.name]+=individualAmount
                mainUser.toReceive[user.name]+=individualAmount
                continue
            user.toPay[mainUser.name]=individualAmount
            mainUser.toReceive[user.name]=individualAmount

    def splitExact(self,totalAmount,amountList,mainUser,sharingPersonsList):
        if not totalAmount==sum(amountList):
            print("Invalid Input")
            return
        for idx,user in enumerate(sharingPersonsList):
            if mainUser.name in user.toPay:
                user.toPay[mainUser.name]+=amountList[idx]
                mainUser.toReceive[user.name]+=amountList[idx]
                continue
            user.toPay[mainUser.name]=amountList[idx]
            mainUser.toReceive[user.name]=amountList[idx]
    
    def splitPercent(self,totalAmount,mainUser,sharingPersonsList,percentageSplitList):
        if not sum(percentageSplitList)==100:
            print("Invalid Input")
            return 
        for idx,user in enumerate(sharingPersonsList):
            if mainUser.name in user.toPay:
                user.toPay[mainUser.name]+=int(percentageSplitList[idx]/100*totalAmount)
                mainUser.toReceive[user.name]+=int(percentageSplitList[idx]/100*totalAmount)
                continue
            user.toPay[mainUser.name]=int(percentageSplitList[idx]/100*totalAmount)
            mainUser.toReceive[user.name]=int(percentageSplitList[idx]/100*totalAmount)
    
def maintainBalance(userList):
    for user in userList:
        for key in user.toPay:
            if key in user.toReceive:
                if user.toPay[key]>user.toReceive[key]:
                    user.toPay[key]-=user.toReceive[key]
                    user.toReceive[key]=0
                else:
                    user.toReceive[key]-=user.toPay[key]
                    user.toPay[key]=0

def printExpense(userList):
    for user in userList:
        flag=False
        for key in user.toPay:
            if user.toPay[key]!=0:
                flag=True
                break
        if flag:
            print("UserName:",user.name)
            for key in user.toPay:
                print(user.name," owes ",key,":",user.toPay[key])
            print("-----------------------------------")
    print("#Expense Sharing Updated....\n\n")

u1=User(1,"u1")
u2=User(2,"u2")
u3=User(3,"u3")
u4=User(4,"u4")

u1.splitEqual(1000,u1,[u2,u3,u4])
maintainBalance([u1,u2,u3,u4])
printExpense([u1,u2,u3,u4])

u1.splitExact(1250,[370,880],u1,[u2,u3])
maintainBalance([u1,u2,u3,u4])
printExpense([u1,u2,u3,u4])

u4.splitPercent(1200,u4,[u1,u2,u3],[40,20,20,20])
maintainBalance([u1,u2,u3,u4])
printExpense([u1,u2,u3,u4])
