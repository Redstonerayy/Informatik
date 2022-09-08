# Anton Rodenwald Nr.5 am 6.9.22
import re 

# regex for mail
# n amount of lower alphabet characters or ., then @, n amount of lower alphabet characters, then ., n amount of lower alphabet characters
mailalphabet = r"[a-z.]+@[a-z]+\.[a-z]"
mailalphanumerical = r"[a-z0-9.]+@[a-z0-9]+\.[a-z0-9]"
mailwithspecials = r"[a-zA-Z0-9~!$%^&*_=+}{'?\-.]+@[a-z0-9]+\.[a-z0-9]"
unlimitedtld = r"+"

def tldlength(min, max):
    return "{" + str(min) + "," + str(max) + "}"

# define function which return the result of the regex
def ismailvalid(address, tld, numbers=False, special=False) -> bool: 
    if special:
        match = re.match(mailwithspecials + tld, address)
    elif numbers:
        match = re.match(mailalphanumerical + tld, address)
    else:
        match = re.match(mailalphabet + tld, address)
    
    if match:
        return match.group() == address
    else:
        return False


adresses = [
	"monopole@me.com",
	"jbailie@me.com",
	"cgcra@live.com",
	"cparis@verizon.net",
	"bree1gster@hotmail.com",
	"pain1a@sbc1global.net",
	"fglock@msn.c1om",
	"gat=1or@outlook.com1",
	"mcs+porran@aol.co1m",
	"mu?ns_1on@comcast.net",
	"ara!thi@ya1hoo.com",
	"tryg$@1stad@comcast.net",
]

# test regex
for i in adresses:
	print(ismailvalid(i, tldlength(1,2), False, False))
