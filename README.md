# Project Title

random-fail is a simple tool for testing random container failures.

### Details

It generates a random number between 1, 100. If the random number
is <= the number passed on the command line, the process exits
with exit code 1, otherwise it exits with exit code 0.

Essentially, the larger the number passed on the command line,
the more probability of the container failing.

Passing 0 on the command line will guarantee that the container
always succeeds.

### Running random-fail

```
docker run -it shrinand/random-fail /run.py 50
```

