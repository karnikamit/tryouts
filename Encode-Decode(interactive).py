#Decode and Encode
import simpleguitk

CIPHER = {'-':'-','|':'|', 'a': 'b', 'b':'c','c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i', 'i':'j', 'j':'k', 'k':'l', 'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 'x':'y', 'y':'z', 'z':'1'}
message = " "
emsg = ''
dmsg = ''
a,b = '', ''
#Encode button
def encode():
    global message, emsg,a
    for ch in message:
        emsg += CIPHER[ch]
    a = message, 'encodes to', emsg

#Decode button
def decode():
    global message, dmsg, b
    for ch in message:
        for key in CIPHER:
            if ch == CIPHER[key]:
                dmsg += key
    b = message, 'decodes to', dmsg

#Update new message
def newmsg(msg):
    global message
    messa = msg
    messag = messa.strip().replace(' ', '-')
    message = messag.strip().replace('\n', '|')
    #label.set_text(msg)

def draw(canvas):
    global message, emsg, dmsg, a, b
    canvas.draw_text(a, [10, 50], 15, 'White')
    canvas.draw_text(b, [10, 100], 15, 'White')
def newcode():
    global message, emsg, dmsg, a, b
    message = " "
    emsg = ''
    dmsg = ''
    a,b = '', ''
    

#Create a frame
frame = simpleguitk.create_frame('Criptography', 500, 200)
frame.set_draw_handler(draw)
frame.add_input("Enter the 'Message' and hit 'Return'", newmsg, 200)
#label = frame.add_label("", 200)
frame.add_button("Encode", encode, 200)
frame.add_button("Decode", decode, 200)
frame.add_button("New Code", newcode, 200)
#Start the frame
frame.start()
