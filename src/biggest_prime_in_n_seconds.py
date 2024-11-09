import time
import sys

limit = int(input("Enter a time limit in seconds: "))

start = time.time()

primes = []

i = 2

try:
    while time.time() - start < limit:
        if "--progress" in sys.argv:
            print(f"Progress: {((time.time() - start) * 100)/ limit:.2f}%", end="\r", flush=True)
        for n in primes:
            if i % n == 0:
                if sys.argv[-1] in ["-vv", "-vvv"]:
                    print(i, "is not prime", end="\r", flush=True)
                break
        else:
            if sys.argv[-1] in ["-v", "-vv", "-vvv"]:
                print(i, "is prime", end="\r", flush=True)
            primes.append(i)
        i += 1
except KeyboardInterrupt:
    print("\nINTERRUPTED")
print(f"The biggest prime in {(time.time() - start):.2f} seconds is:\n{primes[-1]}, the {len(primes)}th prime")
