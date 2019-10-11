# -*- coding: utf-8 -*-
import nltk
from nltk.tag import RegexpTagger
import pyarabic.araby as araby
import re

class NLPAR:

    p1=[u'ل',u'ب',u'ف',u'س',u'و',u'ي',u'ت',u'ن',u'ا']
    p2=[u'ال',u'لل']
    p3=[u'وال',u'ولل',u'كال',u'بال']
    pf=[u'سا',u'سن',u'ست',u'سي',u'ين',u'تن',u'نن']
    s1=[u'ة',u'ه',u'ي',u'ك',u'ت',u'ا',u'ن']
    s2=[u'هم',u'ما',u'وا',u'ني',u'كن',u'تم',u'ها',u'يا',u'نا',u'هن',u'كم',u'تن',u'ين',u'ان',u'ات',u'ون']
    s3=[u'كمل',u'تين',u'تان',u'همل',u'تمل']

    def ARTokenizer(self, sent):
        L = nltk.word_tokenize(sent)
        return L

    def removeSuffixes(self, tmp):
        tmp2=''
        for i in self.s3:
            if tmp.endswith(i):
                 a=3
                 tmp2=tmp[0:-a]
                 return tmp2
        for i in self.s2:
            if tmp.endswith(i):
                a=2
                tmp2=tmp[0:-a]
                return tmp2
        for i in self.s1:
            if tmp.endswith(i):
                a=1
                tmp2=tmp[0:-a]
                return tmp2
        return tmp

    def removePrefixes(self, tmp):
        tmp2=''
        for i in self.p3:
            if tmp.startswith(i):
                a=3
                tmp2=tmp[a:]
                return tmp2
        for i in self.p2:
            if tmp.startswith(i):
                a=2
                tmp2=tmp[a:]
                return tmp2        
        for i in self.pf:
            if tmp.startswith(i):
                a=2
                tmp2=tmp[a:]
                return tmp2
        for i in self.p1:
            if tmp.startswith(i):
                a=1
                tmp2=tmp[a:]
                return tmp2
        return tmp

    #check length four patterns
    def checkP4(self, tmp):
        if re.search(r'^م[ا-ي]{3}$',tmp):
            #"مفعل"
            tmp2=tmp[1]+tmp[2]+tmp[3]
        elif re.search(r'^[ا-ي]{2}و[ا-ي]$',tmp):
            #"فعول"
            tmp2=tmp[0]+tmp[1]+tmp[3]
        elif re.search(r'^[ا-ي]{3}ة$',tmp):
            #"فعلة"
            tmp2=tmp[0]+tmp[1]+tmp[2]
        elif re.search(r'^[ا-ي]{2}ا[ا-ي]$',tmp):
            #"فعال"
            tmp2=tmp[0]+tmp[1]+tmp[3]
        elif re.search(r'^[ا-ي]{2}ي[ا-ي]$',tmp):
            #"فعيل"
            tmp2=tmp[0]+tmp[1]+tmp[3]
        elif re.search(r'^[ا-ي]ا[ا-ي]{2}$', tmp):
            #"فاعل"
            tmp2=tmp[0]+tmp[2]+tmp[3]                       
        else:
            tmp2=''
        return tmp2

    #check length five patterns and length three root
    def checkP53(self, tmp):
        tmp2=''
        if re.search(r'^ت[ا-ي]ا[ا-ي]{2}$',tmp):
                    #"تفاعل"
                    tmp2=tmp[1]+tmp[3]+tmp[4]
        elif re.search(r'^ا[ا-ي]ت[ا-ي]{2}$',tmp):
                    #"افتعل"
                    tmp2=tmp[1]+tmp[3]+tmp[4]
        elif re.search(r'^ا[ا-ي]{2}ا[ا-ي]$',tmp):
                    #"افعال"
                    tmp2=tmp[1]+tmp[2]+tmp[4]
        elif re.search(r'^ا[ا-ي]ا[ا-ي]{2}$',tmp):
                    #"افاعل"
                    tmp2=tmp[1]+tmp[3]+tmp[4]
        elif re.search(r'^[ا-ي]{2}ا[ا-ي]ة$',tmp):
                    #"فعالة"
                    tmp2=tmp[0]+tmp[1]+tmp[3]
        elif re.search(r'^[ا-ي]{3}ان$',tmp):
                    #"فعلان"
                    tmp2=tmp[0]+tmp[1]+tmp[2]
        elif re.search(r'^[ا-ي]{2}و[ا-ي]ة$',tmp):
                    #"فعولة"
                    tmp2=tmp[0]+tmp[1]+tmp[3]
        elif re.search(r'^ت[ا-ي]{3}ة$',tmp):
                    #"تفعلة"
                    tmp2=tmp[1]+tmp[2]+tmp[3]
        elif re.search(r'^ت[ا-ي]{2}ي[ا-ي]$',tmp):
                    #"تفعيل"
                    tmp2=tmp[1]+tmp[2]+tmp[4]
        elif re.search(r'^م[ا-ي]{3}ة$',tmp):
                    #"مفعلة"
                    tmp2=tmp[1]+tmp[2]+tmp[3]
        elif re.search(r'^م[ا-ي]{2}و[ا-ي]$',tmp):
                    #"مفعول"
                    tmp2=tmp[1]+tmp[2]+tmp[4]
        elif re.search(r'^[ا-ي]ا[-ي]و[ا-ي]$',tmp):
                    #"فاعول"
                    tmp2=tmp[0]+tmp[2]+tmp[4]
        elif re.search(r'^[ا-ي]وا[ا-ي]{2}$',tmp):
                    #"فواعل"
                    tmp2=tmp[0]+tmp[3]+tmp[4]
        elif re.search(r'^م[ا-ي]{2}ا[ا-ي]$',tmp):
                    #"مفعال"
                    tmp2=tmp[1]+tmp[2]+tmp[4]
        elif re.search(r'^م[ا-ي]{2}ي[ا-ي]$',tmp):
                    #"مفعيل"
                    tmp2=tmp[1]+tmp[2]+tmp[4]
        elif re.search(r'^ا[ا-ي]{3}ة$',tmp):
                    #"افعلة"
                    tmp2=tmp[1]+tmp[2]+tmp[3]
        elif re.search(r'^[ا-ي]{2}ائ[ا-ي]$',tmp):
                    #"فعائل"
                    tmp2=tmp[0]+tmp[1]+tmp[4]
        elif re.search(r'^من[ا-ي]{3}$',tmp):
                    #"منفعل"
                    tmp2=tmp[2]+tmp[3]+tmp[4]
        elif re.search(r'^م[ا-ي]ت[ا-ي]{2}$',tmp):
                    #"مفتعل"
                    tmp2=tmp[1]+tmp[3]+tmp[4]
        elif re.search(r'^[ا-ي]ا[ا-ي]{2}ة$',tmp):
                    #"فاعلة"
                    tmp2=tmp[0]+tmp[2]+tmp[3]
        elif re.search(r'^م[ا-ي]ا[ا-ي]{2}$',tmp):
                    #"مفاعل"
                    tmp2=tmp[1]+tmp[3]+tmp[4]
        elif re.search(r'^[ا-ي]م[ا-ي]ا[ا-ي]$',tmp):
                    #"فملاع"
                    tmp2=tmp[0]+tmp[4]+tmp[2]
        elif re.search(r'^ي[ا-ي]ت[ا-ي]{2}$',tmp):
                    #"يفتعل"
                    tmp2=tmp[1]+tmp[3]+tmp[4]
        elif re.search(r'^ت[ا-ي]ت[ا-ي]{2}$',tmp):
                    #"تفتعل"
                    tmp2=tmp[1]+tmp[3]+tmp[4]
        elif re.search(r'^[ا-ي]{2}ا[ا-ي]ي$',tmp):
                    #"فعالي"
                    tmp2=tmp[0]+tmp[1]+tmp[3]
        elif re.search(r'^ان[ا-ي]{3}$',tmp):
                    #"انفعل"
                    tmp2=tmp[2]+tmp[3]+tmp[4]
        else:
            tmp2=''
        return tmp2

    #check length five patterns and length four root
    def checkP54(self, tmp):
        tmp2=''
        if re.search(r'^ت[ا-ي]{4}$',tmp):
                    #"تفعلل"
                    tmp2=tmp[1:]
        elif re.search(r'^ا[ا-ي]{4}$',tmp):
                    #"افعلل"
                    tmp2=tmp[1:]
        elif re.search(r'^م[ا-ي]{4}$',tmp):
                    #"مفعلل"
                    tmp2=tmp[1:]
        elif re.search(r'^[ا-ي]{4}ة$',tmp):
                    #"فعللة"
                    tmp2=tmp[0]+tmp[1]+tmp[2]+tmp[3]
        elif re.search(r'^[ا-ي]{3}ان$',tmp):
                    #"فعلان"
                    tmp2=tmp[0]+tmp[1]+tmp[2]
        elif re.search(r'^[ا-ي]{2}ائ[ا-ي]$', tmp):
                    #"فعالل"
                    tmp2=tmp[0]+tmp[1]+tmp[4]
        else:
            tmp2=''
        return tmp2

    #check length six patterns and length three root
    def checkP63(self, tmp):
        tmp2=''
        if re.search(r'^است[ا-ي]{3}$',tmp):
                    #"استفعل"
                    tmp2=tmp[3]+tmp[4]+tmp[5]
        elif re.search(r'^م[ا-ي]{2}ا[ا-ي]ة$',tmp):
                    #"مفعالة"
                    tmp2=tmp[1]+tmp[2]+tmp[4]
        elif re.search(r'^ا[ا-ي]ت[ا-ي]ا[ا-ي]$',tmp):
                    #"افتعال"
                    tmp2=tmp[1]+tmp[3]+tmp[5]
        elif re.search(r'^ا[ا-ي]{2}و[ا-ي]{2}$',tmp):
                    #"افعوعل"
                    tmp2=tmp[1]+tmp[2]+tmp[5]
        elif re.search(r'^ان[ا-ي]{3}$',tmp):
                    #"انفعل"
                    tmp2=tmp[2:]
        elif re.search(r'^مست[ا-ي]{3}$', tmp):
                    #"مستفعل"
                    tmp2=tmp[3:]
        else:
            tmp2=''
        return tmp2

    def len4(self, tmp):
        #If the word matches one of the patterns from checkP4
        tmp2=self.checkP4(tmp)
        if tmp2:
            return tmp2
        #Otherwise, attempt to remove length-one suffixes and prefixes from S1 and P1 in that order to get a word not less than three letters in length
        else:            
            for i in self.s1:
                if tmp.endswith(i):
                    a=1
                    tmp2=tmp[0:-a]
                    return tmp2
            for i in self.p1:
                if tmp.startswith(i):
                    a=1
                    tmp2=tmp[a:]
                    return tmp2
    
    def len5(self, tmp):
        #If the word matches one of the patterns from checkP53
        tmp2=self.checkP53(tmp)
        if tmp2:
            return tmp2
        #remove suffixes and prefixes
        tmp2=tmp
        tmp2=self.removeSuffixes(tmp2)
        tmp2=self.removePrefixes(tmp2)
        #If the relevent length-three stem is returned
        if len(tmp2) == 3:
            return tmp2
        #If the word still five characters in length, the word matches checkP54
        elif len(tmp) == 5:
            tmp2=tmp
            tmp2=self.checkP54(tmp)
            return tmp2
        return "error"

    def len6(self, tmp):
        tmp3=''
        #If the word matches one of the patterns from checkP63
        tmp2=self.checkP63(tmp)
        if tmp2:
            return tmp2
        #remove suffixes
        tmp2=tmp
        tmp2=self.removeSuffixes(tmp2)
        if len(tmp2)==4:
            tmp2=self.len4(tmp2)
            return tmp2
        elif len(tmp2)==5:
            tmp2=self.len5(tmp2)
            return tmp2
        else:
            for i in self.p1:
                if tmp2.startswith(i):
                    a=1
                    tmp3=tmp2[a:]
            if len(tmp3)==5:
                tmp2=self.len5(tmp2)
                return tmp2

    def len7(self, tmp):
        tmp2=''
        #Remove one-character suffixes and prefixes
        for i in self.s1:
            if tmp.endswith(i):
                a=1
                tmp2=tmp[0:-a]        
        for i in self.p1:
            if tmp.startswith(i):
                a=1
                tmp2=tmp[a:]
        if len(tmp2)==4:
            tmp2=self.len4(tmp2)
            return tmp2
        elif len(tmp2)==5:
            tmp2=self.len5(tmp2)
            return tmp2
        elif len(tmp2)==6:
            tmp2=self.len6(tmp2)
            return tmp2

    def ARStemmer(self, word):
        #Remove diacritics representing vowels
        res = araby.strip_tashkeel(word)
        #Normalize the hamza which appears in several distinct forms in combination with various letters to one form “أ”
        tmp=''
        for i in res:
            if i in araby.HAMZAT:
                tmp+=u'أ'
            else:
                tmp+=i
        #Remove length 2 and 3 prefixes
        for i in self.p2:
            if tmp.startswith(i):
                a=2
                tmp2=tmp[a:]
                break
            else:
                    tmp2=tmp
        tmp=tmp2
        for i in self.p3:
            if tmp.startswith(i):
                a=3
                tmp2=tmp[a:]
                break
            else:
                                tmp2=tmp
        tmp=tmp2
        #Remove connector “و” if it precedes a word beginning with “و".
        if tmp.startswith(u'وو'):
                a=1
                tmp2=tmp[a:]
        else:
                tmp2=tmp
        tmp=tmp2

        #Normalize “أ,آ,إ”to “ا”
        tmp2=''
        for i in tmp:
            if i in araby.ALEFAT:
                tmp2+=u'ا'
            else:
                tmp2+=i
        tmp=tmp2

        a = len(tmp)
        if a == 3:
                #Return stem if less than or equal to three
                tmp2=tmp
        elif a == 4:
                tmp2=self.len4(tmp)
        elif a == 5:
                tmp2=self.len5(tmp)
        elif a == 6:
                tmp2=self.len6(tmp)          
        elif a == 7:
                tmp2=self.len7(tmp)
        return tmp2
		
    def ARPosTag(self, List):        
        patterns = [
            ('^(الله|لله|ربنا|رب|إله)$','لفظ جلالة'),
            ('^(به|فيه|عنه|إليه|اليه|كل|بعض)$','حرف'),
            ('^(هذا|هذه|هذان|هاتان|هؤلاء|تلك|أولئك)$', 'اسم إشارة'),
            ('^(ثم|حتا|أو|أم|لكن|لا|مع)$', 'حرف عطف'),
            ('^(من|إلى|الى|عن|على|في|فى)$', 'حرف جر'),
            ('^(هى|هو|هي|هما|هم|هن)$', 'ضمير غائب'),
            ('^(أنت|أنتما|أنتم|أنتن|إياك|إياكما|إياكم|إياكن)$', 'ضمير متكلم'),
            ('^(كان|اصبح|أصبح|أمسى|امسى|ظل|اضحى|أضحى|بات|صار|ليس|ما زال|ما برح|ما انفك|ما دام|ما فتئ)$','كان وأخواتها'),
            ('^(إن|أن|ان|كأن|لكن|لعل|ليت)$','إن وأخواتها'),
            ('^(هل|من|أي|ما|ماذا|متى|أين|كيف|كم|لماذا|أنى|أيان)$', 'حرف /اسم استفهام'),
            ('^(حين|صباح|ظهر|ساعة|سنة|أمس|مساء)$', 'ظرف زمان'),
            ('^(فوق|تحت|أمام|وراء|حيث|دون)$', 'ظرف مكان'),
            ('^(الذي|التي|اللذان|اللتان|الذين|اللاتي|اللواتي|اللائي)$', 'اسم موصول'),
            ('([ا-ي]{3}ان)|([ا-ي]{3}ى)|([ا-ي]{3}ء)|[أا]حمر|[أا]صفر|[أا]خضر|رمادي|[أا]سود|[أا]زرق','صفة'),
            #('^([ا-ي]{2}ا[ا-ي])$|^([ا-ي]{2}و[ا-ي])$|^([ا-ي]{2}ي[ا-ي])$','صفة مشبهه باسم فاعل'),
            ('^([ا-ي]{3}ة)$|^(م[ا-ي]{2}و[ا-ي])$','اسم مفعول'),
            ('^(م[ا-ي]{3})$','اسمي الزمان والمكان'),
            ('^س?[نايت][ا-ي]{3,4}$|^[ا-ي]{3,4}$|^س?[نايت][ا-ي]ا[ا-ي]{2}$|^س?[نايت]ن[ا-ي]{3}$|^س?[نايت]ت[ا-ي]ا[ا-ي]{2}$|^[نايت]ست[ا-ي]{3}$|^[نايت]ت[ا-ي]{4}$','فعل'),
            ('^((وال)|(فال)|(بال)|(كال)|(ال)).+|^ت[ا-ي]{2}ي[ا-ي]$|^[ا-ي]{2}[واي][ا-ي]$', 'اسم'),
            ('.+((ائي)|(انك)|(انه)|(اؤك)|(اؤه)|(اءك)|(اءه)|(هما)|(كما)|(ات)|(ة))$|^[ا-ي]ا[ا-ي]{2}ة?$', 'اسم'),
            ('','اسم'),
        ]
        reg = RegexpTagger(patterns)

        tmpList = []
        for k in List:
            tmp = araby.strip_tashkeel(k)
            tmp2=''
            for i in self.s2:
                if tmp.endswith(i):
                    a=2
                    tmp2=tmp[0:-a]
                else:
                    tmp2=tmp
            tmpList.append(tmp2)        
        return reg.tag(tmpList)  
        
'''        
print("بدأ")

ob = NLPAR()
#sent = u'فعلت ينفعل تشغيل ألعابك لعوب لعبة لعيب مأكل مأكول وورد والجالسون سأذهب يلعبون ستلعبون مؤمن أَنا أُحِبُ الألوان يِلعَّب'
sent = u'منزل تلعب  محمود فعال فعول فعيل أزرق سمير كريم فعلان عطشان هي فتاة تحب الكتابة'
#sent=u'المعلم رائد التربية فى كل عصر أساس نهضة الأمة'

L = ob.ARTokenizer(sent)
P = ob.ARPosTag(L)

for i in range(len(L)):
        w = ob.ARStemmer(L[i])
        print ("(" + L[i] + "), (" + w + "),  (" + P[i][1]+")")
        #print ("الكلمة: " + L[i] + " , مصدرها: " + w + " , نوعها: " + P[i][1])
'''