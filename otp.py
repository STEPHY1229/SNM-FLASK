# write once read many times ==> modulization
import random
def genotp():
    otp=''
    u_l=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    s_l=[chr(i) for i in range(ord('a'),ord('z')+1)]
    for i in range(2):
        otp=otp+random.choice(u_l)+str(random.randint(0,9))+random.choice(s_l)
    return otp








# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>OTP</title>
#     <link rel="stylesheet" href="{{ url_for('static', filename='welcome.css') }}">
# </head>
# <body>
#     <form class="myForm">
#         <h1>ONE TIME PASSWORD</h1>
#         <label>OTP:</label>
#         <input type="email" placeholder="Enter OTP" required>
#     </form>
#     <!--<div class="last">
#             <a href="#"><button>REGISTER</button></a>
#             <a href="./register.html"><button>LOGIN</button></a> 
#         </div>-->
# </body>
# </html>