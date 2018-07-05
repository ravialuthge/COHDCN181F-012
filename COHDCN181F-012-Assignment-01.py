import sys,os
text_list=[]
if len(sys.argv) == 2:                                         #.\COHDCN181F-012-Assignment-01.py filename.txt
        if os.path.isfile(sys.argv[1]):
            
            f =open(str(sys.argv[1]),'r')
            rawcon = f.read()
            f.close()
            def func(text):
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

            def replace_line(word):
                new_word=""
                for i in str(word):
                        if i=="\n":
                                new_word+="."
                        else:
                                new_word+=i
                return new_word

            def line(val):
                  return "0"*(7-len(str(hex(val))[2:]))+str(hex(val))[2:]+"0"
            text=""
            count=0
            for i in str(rawcon):
                text+=i
                count+=1
                if count == 16:
                        text_list.append(text) 
                        count=0
                        text=" "
           
            for i in range(len(text_list)):
                  print(line(i),func(text_list[i])[0:41] + " ",str(replace_line(text_list[i])[0:16]))
            
            
        else:
          print("No such file or directory")
else:
        print("invalid command")
