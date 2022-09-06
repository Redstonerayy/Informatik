# Anton Rodenwald Nr.5 am 6.9.22
import re 

# regex for mail
# n amount of lower alphabet characters or ., then @, n amount of lower alphabet characters, then ., n amount of lower alphabet characters
mailvalid = r"[a-z.]+@[a-z]+\.[a-z]+"

# define function which return the result of the regex
def ismailvalid(address) -> bool: 
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

# test regex
for i in adresses:
	print(ismailvalid(i))
