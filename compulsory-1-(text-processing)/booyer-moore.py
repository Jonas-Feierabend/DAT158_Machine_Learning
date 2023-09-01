text = "Die Pferde (Equus) sind die einzige rezente Gattung der Familie der Equidae. Zur Gattung gehören die Wildpferde (das Przewalski-Pferd und der heute ausgestorbene Tarpan), die verschiedenen Wildeselformen (der Afrikanische und der Asiatische Esel beziehungsweise der Kiang) sowie wenigstens drei Zebra-Arten (das Steppen-, das Berg- und das Grevyzebra). Sie schließt auch die aus den Wildtieren domestizierten Hausformen ein. Die Anzahl der Arten und ihre Abgrenzung zueinander sind bis heute umstritten. Insgesamt werden häufig sieben oder acht Arten unterschieden, von denen die Mehrzahl in ihrem Bestand gefährdet ist. Die Tiere leben heute in Afrika südlich der Sahara und im südlichen sowie zentralen und östlichen Asien. Die bewohnten Habitate bestehen aus offenen, häufig grasbestandenen Landschaftsräumen, die mitunter auch sehr trocken bis wüstenartig sein können. An diese Regionen sind Pferde durch ihren kräftigen Körperbau und die langen, schlanken Gliedmaßen angepasst. An den Beinen findet sich auch das kennzeichnende Merkmal der Gattung, da sowohl die Vorder- als auch die Hinterfüße jeweils nur eine Zehe aufweisen, die von einem breiten Huf bedeckt wird. Der Rückgang der Zehenanzahl, der den Pferden auch die höherrangige Bezeichnung „Einhufer“ einbrachte, ermöglicht eine schnelle und reibungsarme Fortbewegung in den Steppen- und Savannengebieten.Generell sind Pferde gesellig lebende Tiere. Es lassen sich zwei Gruppentypen in der Sozialgemeinschaft unterscheiden: einer mit Mutter-Jungtiergruppen und einzeln lebenden Hengsten und ein zweiter mit größeren Gruppen aus Stuten und Jungtieren, die auch ein oder mehrere männliche Tiere mit einschließen, die sogenannten „Harems“. Die Ausbildung des einen oder anderen Grundtyps ist in der Regel von äußeren Faktoren abhängig. Dazu zählt vor allem das Nahrungsangebot, das über das Jahr beständig oder – durch den stärkeren Einfluss von Jahreszeiten – auch wechselnd sein kann. Die Hauptnahrung der Tiere besteht aus Gräsern, gelegentlich fressen sie auch Blätter und Zweige. Zum Zerkauen der harten Grasnahrung bildeten sich bei den Pferden Backenzähne mit extrem hohen Zahnkronen heraus, was als ein weiteres typisches Kennzeichen der Gattung herangezogen wird. Der im Vergleich zu anderen Huftieren weniger effiziente Magen-Darm-Trakt bedingt, dass die Pferde den größten Teil ihrer aktiven Zeit mit der Nahrungsaufnahme verbringen. Die Hengste verpaaren sich mit mehreren Stuten, während die Stuten, abhängig von dem sozialen Gruppentyp, in dem sie leben, entweder einen oder mehrere Hengste als Paarungspartner haben. Zumeist wird ein einzelnes Fohlen geboren, das nach maximal sechs Jahren selbständig ist. Der männliche wie auch der weibliche Nachwuchs verlässt anschließend die elterliche Gruppe."
pattern = "Pferde"


def last(c,pattern):
    """the last function calculates the last 
    occurence of a pattern in a text (or another pattern)"""
    return pattern.rfind(c)


def boyer_moore(pattern,text): 
    i = len(pattern) -1 # text iterator 
    j = len(pattern)-1 #pattern iteartor
    comparisions = 0
    
    
    while True:
        
        if(pattern[j] == text[i]):
            comparisions += 1  
            if(j == 0):
                return [i,comparisions, comparisions/len(pattern)]
            else:
                j-=1
                i-=1

        else:
            i = i+len(pattern) - min(j,last(text[i],pattern)+1) 
            j = len(pattern)-1

        if(i >len(text)-1):
            break

    return [-1,comparisions,comparisions/len(pattern)]

i,comp,comp_p_char = boyer_moore(pattern,text)
print("Found at position"+ str(i)+ "\n Comparisions: "+ str(comp) )
print("comparisons/char: "+ str(comp_p_char))
