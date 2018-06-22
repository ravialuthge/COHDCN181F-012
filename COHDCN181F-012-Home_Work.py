sum = 0
def cal():
     if sum>=2000:
                discount=sum*0.10
                n=sum-discount
                        
     elif sum>=1500:
                discount=sum*0.07
                n=sum-discount
                      
     elif sum>=1000:
                discount=sum*0.05
                n=sum-discount
                     
     else:
                discount=0
                n=sum
     
     print("Sum :%.2f" %sum)           
     print("Discount :%.2f" %discount)
     print("Net Total :%.2f" %n)
     return file(discount,n)
     
def file(discount,n):
   file = open('bill.txt', 'w')
   file.write("Sum:")
   file.write(str(sum))
   file.write("\n")
   file.write("Discount:")
   file.write(str(discount))
   file.write("\n")
   file.write("Net Total:")
   file.write(str(n)) 
   file.close()
   
while True:
        try:
            num = str(input("Enter Price:"))
            sum = float(sum) + float(num)
            errorvalue = False
        except ValueError:
            if num == "":      
                break
            errorvalue = True
        if errorvalue:
            print("invalid")
cal()
