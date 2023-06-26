# RSA Factoring Challenge

This project aims to factorize numbers into a product of two smaller numbers. The motivation behind this challenge is to decrypt encrypted documents by identifying numbers that are not generated using large enough prime numbers. The goal is to factorize these numbers as quickly as possible before the target fixes the bug on their server.

## Getting Started

To participate in this project, follow these steps:

1. Clone the GitHub repository: [RSA-Factoring-Challenge](https://github.com/your-username/RSA-Factoring-Challenge).
2. Review the provided resources to gain an understanding of RSA, HTTPS security, and prime factorization.
3. Familiarize yourself with the project requirements and tasks outlined below.
4. Implement the required functionality in the programming language of your choice.
5. Push all your scripts, source code, and other relevant files to your repository.

## Project Requirements

- Language: You can choose the programming language of your preference.
- Operating System: Standard Ubuntu 20.04 LTS.
- Dependencies: Your program should run without any external dependencies. You cannot install additional packages on the machine where your program will be executed.

## Tasks

### Task 0: Factorize All the Things!

Implement a program that factors as many numbers as possible into a product of two smaller numbers. The program should read numbers from a file and output the factorization results.

#### Usage

```
factors <file>
```

- `<file>`: A file containing natural numbers to factorize. Each number should be on a separate line, with no empty lines or spaces before/after the number. The file will always end with a new line.

#### Output Format

For each number, the program should output the factorization result in the format `n=p*q`, where `n` is the original number, and `p` and `q` are the smaller factors.

#### Example

Input file (`tests/test00`):
```
4
12
34
128
1024
4958
1718944270642558716715
9
99
999
9999
9797973
49
239809320265259
```

Output:
```
4=2*2
12=6*2
34=17*2
128=64*2
1024=512*2
4958=2479*2
1718944270642558716715=343788854128511743343*5
9=3*3
99=33*3
999=333*3
9999=3333*3
9797973=3265991*3
49=7*7
239809320265259=15485783*15485773
```

### Task 1: RSA Factoring Challenge

This task is an extension of Task 0, but with additional constraints.

Implement a program that factors a single RSA number `n` into two prime numbers `p` and `q`.

#### Usage

```
rsa <file>
```

- `<file>`: A file containing a single RSA number to factorize.

#### Output Format

The program should output the factorization result in the format `n=p*q`, where `n` is the original number, and `p` and `q` are prime numbers.

#### Example

Input file (`tests/rsa-1`):
```
6
```

Output:
```
6=3*2
```

## Time Limit

Your program will be killed if it doesn't finish within 5 seconds.

## Conclusion

This project provides an opportunity to practice prime factorization techniques and contribute to the decryption of encrypted documents. By participating in this challenge, you can earn extra credit and improve your average score
