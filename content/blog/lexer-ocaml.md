---
title: Writing a lexer for C in Ocaml
---

ref. [Nora Sandler's, Writing a C Compiler, Part 1](https://norasandler.com/2017/11/29/Write-a-Compiler.html)

This is my first time using Ocaml, and Dune. First, I'd say install Ocaml and Dune and let's move forward directly with writing a new lexing function in `lexer.ml` that can parse `int main() { return 42; }`.

Second, we want to define what the tokens are. For such a simple program, there are only a handful of tokens we need. Some may call this process "scanning", as does Robert Nystrom [here](https://craftinginterpreters.com/scanning.html), but what it does is take a program, and break it into chunks without worrying about the syntax. For our program, we just need `int, return, {}, (), int, indentation`, roughly.

```ocaml
type token =
  | Int
  | Return
  | LBrace
  | RBrace
  | LParen
  | RParen
  | Number of int
  | Ident of string
```

This might look odd, but is a perfect starting point to Ocaml's weird, quirky style.

The `|` symbol is used in Ocaml to denote various cases a variable can take up. In C, an equivalent program can be

```C
typedef enum {
    Int,
    Return,
    LBrace,
    RBrace,
    LParen,
    RParen,
    Number,
    Ident
} TokenType;

typedef struct {
    TokenType type;
    union {
        int intValue;
        char* strValue;
    } value;
} Token;
```

Moving on, `Int, Return, LBrace, RBrace, LParen, RParen` are simple constructors. They represent a specific kind of token but don't carry any additional data.
`Number of int` and `Ident of string` are constructors with associated data. A token of kind Number carries with it an integer, and a token of kind Ident carries with it a string.

Next, let us define a function named `lex` and function `aux` that takes in a variable named `pos` which we'll use to track where we are inside our argument variable.

```ocaml
let lex str =
  let rec aux pos =
```

We want to make sure that if the position is greater than the length of the input program, we return `[]` from the auxiallry function `aux` that we're using kind of like a faux-indexer.

```ocaml
if pos >= String.length str then []
else
```

Now we want to find a way to containerize the current string into a token. `int` and `i n t` are 1 and 3 tokens, the idea is using the whitespace characters. 

```ocaml
match str.[pos] with | ' ' | '\n' | '\t' | '\r' -> aux (pos + 1)
```

This checks if the 