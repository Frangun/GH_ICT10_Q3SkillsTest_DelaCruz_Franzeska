from pyscript import document, display

# SKILLS TEST ------------------------------------------------

def validate_form(e):
    document.getElementById("output").innerHTML = ' '  
    name = document.getElementById("user").value
    pass_ = document.getElementById("pass").value

    i = name
    p = pass_

    uca = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # uppercase
    num = '0123456789' # numbers

    if len(i) >= 7:  # 7 characters long
        nval = True
    else:
        nval = False

    p2 = False
    p3 = False
    plen = False
    
    if len(p) >= 10:  # 10 characters long
        plen = True
        for char in p:
            if char in uca:   # password --> one uppercase letter
                p2 = True
            if char in num:   # password --> one number
                p3 = True

    if p2 == False and plen == True:
        display(f' **Password must contain at least one UPPERCASE letter! ')
    if p3 == False and plen == True:
        display(f' Password must contain at least ONE NUMBER  !', target='output')
    if plen == False:
        display(f' Password must be at least 10 CHARACTERS long! ', target='output')
        
    pval = p2 and  p3  and  plen    # combination


# PASSWORD
    if pval == True:
        display(f' VALID Password! ', target='output')
    else:
        display(f'INVALID Password, please try again! ', target='output')
    
# USERNAME
    if nval == True:
        display(f'VALID Username! ', target='output')
    else:
        display(f' INVALID Username, please try again! ', target='output')

    if pval == True and nval == True:    #if both are correct 
        display(f' Account Created! ', target='output2')

    
