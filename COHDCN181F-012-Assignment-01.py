import sys,os
text_list=[]
if len(sys.argv) == 2:                            #.\COHDCN181F-012-Assignment-01.py filename.txt
        if os.path.isfile(sys.argv[1]):
            
            f =open(str(sys.argv[1]),'r')
            rawcon = f.read()
            f.close()
            
            def inside_print(value):
                  return "0"*(7-len(str(hex(value))[2:]))+str(hex(value))[2:]+"0"
            text=""
            count=0
            for i in str(rawcon):
                text+=i
                count+=1
                if count == 16:
                        output.append(text) 
                        count=0
                        text=" "
            def enter_con_dot(enter):
                new_word=""
                for i in str(enter):
                        if i=="\n":
                                word1+="."
                        else:
                                word1+=i
                return word1

            def hexdump(text):
                string=""
                for i in str(text):
                        h=str(hex(ord(i)))[2:]
                        string+=h 
                count=0
                string2=": "
                for j in str(string):
                        count+=1
                        string2+=j
                        if count%4==0:
                                string2+=" "
                return string2
           
            for i in range(len(output)):
                  print(inside_print(i),hexdump(text_list[i])[0:41] + " ",str(enter_con_dot(output[i])[0:16]))
            
            
        else:
          print("No such file or directory")
else:
        print("invalid command")

