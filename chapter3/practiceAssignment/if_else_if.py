num =int(input('choose a number 1-7:'))

if num == 1:
    print('monday')
else:
    if num == 2:
        print('tuesday')
    else:
        if num == 3:
            print('wednesday')
        else:
            if num == 4:
                print('Thursday')
            else:
                if num ==5:
                    print('friday')
                else:   
                    if num ==6:
                        print('saturday')
                    else:
                        if num == 7:
                            print('sunday')
                        else:
                            if num>7:
                                print('more than error')
                            else:
                                print('less than error')
