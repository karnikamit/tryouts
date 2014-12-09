import tkinter.filedialog

cipher = {'0':'0', ',':',', '.':'.',  'a': 'b', 'b':'c','c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i', 'i':'j', 'j':'k', 'k':'l', 'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 'x':'y', 'y':'z', 'z':'1',
          'A':'B', 'B':'C', 'C':'D', 'D':'E', 'E':'F', 'F':'G', 'G':'H', 'H':'I', 'I':'J', 'J':'K', 'K':'L', 'L':'M', 'M':'N', 'N':'O', 'O':'P', 'P':'Q', 'Q':'R', 'R':'S', 'S':'T', 'T':'U', 'U':'V', 'V':'W', 'W':'X', 'X':'Y', 'Y':'Z', 'Z':'2'}

def encode():
    al_filename = tkinter.filedialog.askopenfilename()
    wr_filename = tkinter.filedialog.askopenfilename()
    al_file = open(al_filename, 'r')
    wr_file = open(wr_filename, 'w')
    for line in al_file:
        lin = line.strip().replace(" ", '0')
        li = lin.strip().replace("'", "")
        emsg = ''
        for ch in li:
            emsg += cipher[ch]
        wr_file.write('\n')
        wr_file.write(emsg)
    wr_file.close()

encode()
