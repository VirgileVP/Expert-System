# Expert-System

Expert system is a proposal calculation program

## Usage

This program take only 1 argument : file name

```
python3 main.py [file]
```

## Files format

```
Rules1
Rules2
...
Initial facts
Queries
```

### Rules

```
A : A
!A : not A
A + B : A and B
A | B : A or B
A ^ B : A xor (exclusive or) B
A => C : A implies C
a <=> C : A if and only if C
```

### Initial facts

```
=ABC : A, B and C are trues, others are false
```

### Queries

```
?DEF : values of D, E and F ? (true, false or undetermined)
```

### Exemple

```
#this is a comment

#Rules :
C => E
A + B + C => D
A | B => C
A + !B => F
C | !G => H
V ^ W => X
A + B => Y + Z
C | D => X | V
E + F => !V
A + B <=> C
A + B <=> !C

#Initial facts :
=ABG

#Queries :
?GVX 
```
