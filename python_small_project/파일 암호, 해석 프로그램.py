input_number = int(input('1.암호화 2.암호해석 중 선택 : '))
secu = 0
input_filename = input('입력 파일명을 입력해주세요 : ')
input_filepath = "C:/Users/EunJin/Documents/data/"+input_filename
output_filename = input('출력 파일명을 입력하세요 : ')
output_filepath = "C:/Users/EunJin/Documents/data/"+output_filename
inFp = open(input_filepath, 'r', encoding='utf-8')
outFp = open(output_filepath, 'w', encoding='utf-8')
inList = inFp.readlines()
if input_number == 1:
    secu = 100
else:
    secu = -100

while True:
    inStr = inFp.readline()
    if not inStr:
        break
    outStr = ""
    for i in range(0,len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu
        ch2 = chr(chNum)
        outStr = outStr + ch2

    outFp.write(outStr)

inFp.close()
outFp.close()