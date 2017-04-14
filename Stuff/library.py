'''
Created on 06.01.2017

@author: Benny
'''

class library():
    
    wordMap = {"idiot" : "alphakevin",
            "cool" : "fly",
            "freundin" : "bae",
            "ist so" : "isso",
            "Bier" : "Hopfensmoothie",
            "chille" : "hartze/oxidiere",
            "witzig" : "1 nicer lustig",
            "chillen" : "hartzen/rumoxidieren",
            "chill" : "hartz/oxidier",
            "gut" : "gg",
            "Ist das normal" : "IiiiiiiIiIIIiiIIIIiiiIIist das normal?",
            "Boss" : "Babo",
            "berühmt" : "fame",
            "schlecht" : "bg",
            "Viel Spass" : "Gönn dir",}
    
    def addWord(self, name, newWord):
        if not name in self.wordMap:
            self.wordMap[name] = newWord
        
    