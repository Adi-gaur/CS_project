el = False
while el == False:
    print('\t \t \t DATA OPERATIONS')
    print('Operation Want To Perform--')
    print('1- Operation On Strings')
    print('2- Operation On Numbers')
    print('3- Operation On List')
    print('4- Operation On Tuples')
    print('5- Mensuration')
    print('0- Exit')
    
    ch = int(input('Enter Your Choice: '))
    
    # Operations On Strings
    if ch == 1:
        s = input('Enter String To Perform Operation:')
        print('Operation Want To Perform--')
        print('1- Count Vowels And Consonant')
        print('2- Check Palindrom')
        print('3- To print Each Character As Seperate')
        print('4- Count Uppercase, Lowercase, Space, Number and Other Characters')
        print('0- Exit')
    
        ch1 = int(input('Enter Your Choice: '))
        
        # Count Vowels And Consonants
        if ch1 == 1:
            cw = 0
            cc = 0
            for i in s:
                if i in 'AEIOUaeiou':
                    cw += 1
                else:
                    cc += 1
            print('No. Of Vowels: ', cw)
            print('No. Of consonant: ', cc)

        # Check Palindrom
        elif ch1==2:
            rev = ''
            for i in range(len(s)-1, -1, -1):
                rev += s[i]
            if rev==s:
                print('String Is Palindrom')
            else:
                print('String Is Not Palindrom')
        
        #Print Each Character as Seperate 
        elif ch1==3:
            sep = ' - '.join(s)
            print('Seperate Character Of String: ', sep)
        
        # Count Uppercase, Lowercase, Space, number and Other Characters
        elif ch1==4:
            cu = 0
            cl = 0
            cs = 0
            cn = 0
            coc = 0
            for i in s:
                if i.isupper:
                    cu += 1
                elif i.islower:
                    cl += 1
                elif i.isspace:
                    cs += 1
                elif i.isnumeric:
                    cn += 1
                else:
                    coc += 1
            print('No. Of Upper Character: ', cu)
            print('No. Of Lower Character: ', cl)
            print('No. Of Spaces: ' , cs)
            print('No. Of Numeric Character: ', cn)
            print('No. Of Other Character: ', coc)
        
        elif ch1 == 0:
            el = True
            
        else:
            print('Invalid Option')
    
    # Operation On Numbers
    elif ch == 2:
        print('Operation Want To Perform--')
        print('1- Sum  Of Even And Odd Digits Seperately')
        print('2- Check Palindrom')
        print('3- Find Maximum And Minimum No.')
        print('4- Count Prime And Composite Digit')
        print('5- Print Table of The Number')
        print('0- Exit')

        ch2 = int(input('Enter Your Choice: '))
        
        # Sum  Of Even And Odd Digits Seperately
        if ch2 == 1:    
            n = int (input(' Enter Your Number: '))
            se = 0
            so = 0
            while n>0:
                a = n%10
                if a%2==0:
                    se +=a
                else:
                    so += a
                n = n//10
            print('Sum Of Even Digits: ',se)        
            print('Sum Odd Digits: ',so)

        #Check Palindrom 
        if ch2 == 2:
            rev = 0
            n = int(input('Enter Your Number: '))
            while n>0 :
                rev = rev*10 + n%10
                n = n//10
            if rev==n:
                print('Number Is Palindrom')
            else:
                print('Number Is Not Palindrom')
        
        # Find Maximum And Minimum No.
        elif ch2 == 3:
            max = 0
            min = 0
            n1 = int(input('How Many Numbers You Want To Check: '))
            for i in range(n1):
                num = int(input('Enter your Number: '))
                if i==0:
                    max = num
                    min = num
                elif num>max:
                    max = num
                elif num<min:
                    min = num
            print('Maximum Number: ', max)
            print('Minimum Number: ', min)

        # Count Prime And Composite Digit
        elif ch2 == 4:
            cp = 0
            cc = 0
            num = input('Enter your Number: ')
            for i in num:
                if i in '4689':
                    cp += 1   
                elif i in '2357':
                    cc += 1
            print('No. of Prime Number:', cp)
            print('No. of Composite Number:', cc)
        
        # Print Table of The Number
        elif ch2 == 5:
            n = int(input('Enter Your number: '))
            for i in range(10):
                print(n, "x", i+1, "=", n*(i+1))
        
        elif ch2 == 0:
            el = True

        else:
            print('Invalid Option')
    
    # Operation On List
    elif ch == 3:
        l1 = []
        ln = int(input("How Many Items You Want To Enter: "))
        for i in range(ln):
            Element = int (input())
            l1.append(Element)

        print('The Entered List is: ', l1, '\n')
        print('Operation Want To Perform--')
        print('1- Append an Element')
        print('2- Append a List To Given List')
        print('3- Modify an Existing Element')
        print('4- Delete Existing Element')
        print('0- Exit')

        ch3 = int(input('Enter Your Choice:'))
        # Append an Element
        if ch3 == 1:
            ele = int(input("Enter The Element: "))
            l1.append(ele)
            print('New List: ',l1 ,'\n')
        
        # Append a List To Given List
        elif ch3 == 2:
            new_list = list(eval(input('Enter The List To be Appended: ')))
            l1.extend(new_list)
            print('New List: ',l1 ,'\n')
        
        # Modify an Existing Element
        elif ch3 ==3:
            print("list: ", l1) 
            pos = int(input('Enter Position of Element To Modify: '))
            new_element = int(input('Enter New Element; '))
            l1[pos]= new_element
        
        #  Delete Existing Element
        elif ch3 == 4:
            print("list: ", l1)
            ele = int(input('Enter Element To Be Deleted: '))
            l1.remove(ele)             
        
        elif ch3 == 0:
            el = True

        else:
            print('Invalid Option')
    
    # Mensuration
    elif ch == 4:
        print('Operation Want To Perform--')
        print('1- Area Of Circle')
        print('2- Area Of Rectangle')
        print('3- Circumference Of Circle')
        print('4- Area Of Square')
        print('0- Exit')
    
        ch4 = int(input('Enter Your Choice: '))    

        # Area Of Circle
        if ch4 == 1:
            r = int(input('Radius Of Circle: '))
            a = 3.14*r*r
            print('Area Of Circle: ', a )
        
        # Area Of Rectangle
        elif ch4 == 2:
            l = int(input("Length Of Rectangle: "))
            b = int(input("Length Of Breadth: "))
            print('Area Of Recatangle: ', l*b)
        
        # Circumference Of Circle
        elif ch4 == 3:
            r = int(input('Radius Of Circle: '))
            c = 2*(int(3.14*r))
            print('Circumference Of Circle: ', c)
        
        # Area of Square
        elif ch4 == 4:
            s = int(input('Enter Side Of Square: '))
            print('Area Of Square: ', l**2)
        
        elif ch4 == 0:
            el = True

        else:
            print('Invalid Option')
    
    elif ch == 0:
        el = True
    
    else:
        print('Invalid Option')

