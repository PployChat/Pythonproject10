# Exception Handling
# ข้อผิดพลาด การจัดการ
#Exception ข้อผิดพลาดที่เกิดขึ้นตอนโปรแกรมทำงาน
 
try :
    num1 = int( input('ป้อนตัวเลขตัวที่ 1 :'))
    num2 = int( input('ป้อนตัวเลขตัวที่ 2 :'))
 
    sum = num1 + num2
    result = num1 / num2
 
    print(f'ผลรวมของ {num1} + {num2} คือ {sum}')
    print(f'ผลรวมของ {num1} / {num2} คือ {result}')
except ValueError :
    print('ป้อนตัวเลขเท่านั้นห้ามตัวอักษร....สงสัยต้องติดต่อ IT')
except ZeroDivisionError :
    print('ป้อนตัวเลขเท่านั้นห้ามตัวอักษร....สงสัยต้องติดต่อ IT')
except Exception :
    print('มีข้อผิดพลาดเกิดขึี้น ต้องขออภัยอย่างสูง ช่วยติดต่อ IT ด้วยจะแก้ให้')
finally :
    print('Woww....')
    print('Hello...')