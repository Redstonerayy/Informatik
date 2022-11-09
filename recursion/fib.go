package main

func fib(n uint) uint {
	if n < 2 {
		return n
	}
	return fib(n-1) + fib(n-2)
}

func main() {
	// fmt.Println(fib(40))
	fib(40)
}
