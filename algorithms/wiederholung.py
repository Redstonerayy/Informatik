# Anton Rodenwald Nr.5 am 6.9.22
import re 

mailvalid = r"[a-z.]+@[a-z]+\.[a-z]+"

def ismailvalid(address):
	return bool(re.match(mailvalid, address))

adresses = [
	"monopole@me.com",
	"jbailie@me.com",
	"cgcra@live.com",
	"cparis@verizon.net",
	"breegster@hotmail.com",
	"paina@sbcglobal.net",
	"fglock@msn.com",
	"gator@outlook.com",
	"mcsporran@aol.com",
	"munson@comcast.net",
	"arathi@yahoo.com",
	"trygstad@comcast.net",
]

for i in adresses:
	print(ismailvalid(i))