# Exploring Math with Python - Exercise 1-5

import matplotlib

letters = 'abcdefghijklmnopqrstuvwxyz'
indexL = list(letters.upper())
def countLetters(inStr):
    count = []
    for i in range(len(letters)):
        count.append(0)
        
    for c in inStr:
        cLower = c.lower()
        if cLower in letters:
            i = letters.index(cLower)
            count[i] += 1
    return count

def main():
    s = "A man, a plan, a conal - PANAMA!"
    s = 'The Caesar Cipher is a simple shift cipher in which each letter is shifted a certain number of places.  For example, assume that the shift is 7 places, then A is shifted to K, B to L, C to M and the pattern continues until S is shifted to Z.   To shift T through Z, the alphabet is wrapped around (a modulo function) so T is shifted to A, V to B, U to C, up through Z to G.  Given an input text message of  upper case letters, Table 1 identifies the frequency distribution of each letter.  Table 2 identifies the frequency distribution of a message encrypted with a Caesar cipher with a shift of 5 places.  The six most frequently occurring letters are E, T, A, O, I and N, while the six least frequently occurring letters are Z, Q, J, X, K and V.  Table 2 identifies the frequency distribution of a message encrypted with a Caesar cipher with a shift of 5 places.'
    count = countLetters(s)
    print(count)
    matplotlib.pyplot.bar(indexL,count)
    return

main()
            
            
            

