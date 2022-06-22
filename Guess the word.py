import random, os
from time import sleep

#A bunch of words in a list.
_wordList = ['ability', 'able', 'about', 'above',
             'accept', 'according', 'account',
             'across', 'act', 'action',
             'activity', 'actually',
             'add', 'address', 'administration',
             'admit', 'adult', 'affect', 'after',
             'again', 'against', 'age', 'agency',
             'agent', 'ago', 'agree', 'agreement',
             'ahead', 'air', 'all', 'allow', 'almost',
             'alone', 'along', 'already', 'also',
             'although', 'always', 'American', 'among',
             'amount', 'analysis', 'and', 'animal',
             'another', 'answer', 'any', 'anyone', 'anything',
             'appear', 'apply', 'approach', 'area', 'argue',
             'arm', 'around', 'arrive', 'art', 'article',
             'artist', 'ask', 'assume', 'attack', 'attention',
             'attorney', 'audience', 'author', 'authority',
             'available', 'avoid', 'away', 'baby', 'back',
             'bad', 'bag', 'ball', 'bank', 'bar', 'base',
             'beat', 'beautiful', 'because', 'become',
             'bed', 'before', 'begin', 'behavior', 'behind',
             'believe', 'benefit', 'best', 'better', 'between',
             'beyond', 'big', 'bill', 'billion', 'bit', 'black',
             'blood', 'blue', 'board', 'body', 'book', 'born',
             'both', 'box', 'boy', 'break', 'bring', 'brother',
             'budget', 'build', 'building', 'business', 'but',
             'buy', 'call', 'camera', 'campaign', 'can', 'cancer',
             'candidate', 'capital', 'car', 'card', 'care',
             'career', 'carry', 'case', 'catch', 'cause', 'cell',
             'center', 'central', 'century', 'certain', 'certainly',
             'chair', 'challenge', 'chance', 'change', 'character',
             'charge', 'check', 'child', 'choice', 'choose', 'church',
             'citizen', 'city', 'civil', 'claim', 'class', 'clear',
             'clearly', 'close', 'coach', 'cold', 'collection',
             'college', 'color', 'come', 'commercial', 'common',
             'community', 'company', 'compare', 'computer', 'concern',
             'condition', 'conference', 'Congress', 'consider', 'consumer',
             'contain', 'continue', 'control', 'cost', 'could', 'country',
             'couple', 'course', 'court', 'cover', 'create', 'crime',
             'cultural', 'culture', 'cup', 'current', 'customer', 'cut',
             'dark', 'data', 'daughter', 'day', 'dead', 'deal', 'death',
             'debate', 'decade', 'decide', 'decision', 'deep', 'defense',
             'degree', 'Democrat', 'democratic', 'describe', 'design',
             'despite', 'detail', 'determine', 'develop', 'development',
             'die', 'difference', 'different', 'difficult', 'dinner',
             'direction', 'director', 'discover', 'discuss', 'discussion',
             'disease', 'doctor', 'dog', 'door', 'down', 'draw', 'dream',
             'drive', 'drop', 'drug', 'during', 'each', 'early', 'east',
             'easy', 'eat', 'economic', 'economy', 'edge', 'education',
             'effect', 'effort', 'eight', 'either', 'election', 'else',
             'employee', 'end', 'energy', 'enjoy', 'enough', 'enter', 'entire',
             'environment', 'environmental', 'especially', 'establish', 'even',
             'evening', 'event', 'ever', 'every', 'everybody', 'everyone',
             'everything', 'evidence', 'exactly', 'example', 'executive',
             'exist', 'expect', 'experience', 'expert', 'explain', 'eye',
             'face', 'fact', 'factor', 'fail', 'fall', 'family', 'far',
             'fast', 'father', 'fear', 'federal', 'feel', 'feeling', 'few',
             'field', 'fight', 'figure', 'fill', 'film', 'final', 'finally',
             'financial', 'find', 'fine', 'finger', 'finish', 'fire', 'firm',
             'first', 'fish', 'five', 'floor', 'fly', 'focus', 'follow', 'food',
             'foot', 'for', 'force', 'foreign', 'forget', 'form', 'former',
             'forward', 'four', 'free', 'friend', 'from', 'front', 'full',
             'fund', 'future', 'game', 'garden', 'gas', 'general', 'generation',
             'get', 'girl', 'give', 'glass', 'goal', 'good', 'government',
             'great', 'green', 'ground', 'group', 'grow', 'growth', 'guess',
             'gun', 'guy', 'hair', 'half', 'hand', 'hang', 'happen', 'happy',
             'hard', 'have', 'head', 'health', 'hear', 'heart', 'heat',
             'heavy', 'help', 'her', 'here', 'herself', 'high', 'him',
             'himself', 'his', 'history', 'hit', 'hold', 'home', 'hope',
             'hospital', 'hot', 'hotel', 'hour', 'house', 'how', 'however',
             'huge', 'human', 'hundred', 'husband', 'idea', 'identify',
             'image', 'imagine', 'impact', 'important', 'improve', 'include',
             'including', 'increase', 'indeed', 'indicate', 'individual',
             'industry', 'information', 'inside', 'instead', 'institution',
             'interest', 'interesting', 'international', 'interview',
             'into', 'investment', 'involve', 'issue', 'item', 'its',
             'itself', 'job', 'join', 'just', 'keep', 'key', 'kid', 'kill',
             'kind', 'kitchen', 'know', 'knowledge', 'land', 'language',
             'large', 'last', 'late', 'later', 'laugh', 'law', 'lawyer',
             'lay', 'lead', 'leader', 'learn', 'least', 'leave', 'left',
             'leg', 'legal', 'less', 'let', 'letter', 'level', 'lie', 'life',
             'light', 'like', 'likely', 'line', 'list', 'listen', 'little',
             'live', 'local', 'long', 'look', 'lose', 'loss', 'lot', 'love',
             'low', 'machine', 'magazine', 'main', 'maintain', 'major',
             'majority', 'make', 'man', 'manage', 'management', 'manager',
             'many', 'market', 'marriage', 'material', 'matter', 'may', 'maybe',
             'mean', 'measure', 'media', 'medical', 'meet', 'meeting', 'member',
             'memory', 'mention', 'message', 'method', 'middle', 'might',
             'military', 'million', 'mind', 'minute', 'miss', 'mission',
             'model', 'modern', 'moment', 'money', 'month', 'more', 'morning',
             'most', 'mother', 'mouth', 'move', 'movement', 'movie', 'Mrs',
             'much', 'music', 'must', 'myself', 'name', 'nation', 'national',
             'natural', 'nature', 'near', 'nearly', 'necessary', 'need',
             'network', 'never', 'new', 'news', 'newspaper', 'next', 'nice',
             'night', 'none', 'nor', 'north', 'not', 'note', 'nothing',
             'notice', 'now', "n't", 'number', 'occur', 'off', 'offer',
             'office', 'officer', 'official', 'often', 'oil', 'old', 'once',
             'one', 'only', 'onto', 'open', 'operation', 'opportunity',
             'option', 'order', 'organization', 'other', 'others', 'our',
             'out', 'outside', 'over', 'own', 'owner', 'page', 'pain',
             'painting', 'paper', 'parent', 'part', 'participant', 'particular',
             'particularly', 'partner', 'party', 'pass', 'past', 'patient',
             'pattern', 'pay', 'peace', 'people', 'per', 'perform',
             'performance', 'perhaps', 'period', 'person', 'personal',
             'phone', 'physical', 'pick', 'picture', 'piece', 'place',
             'plan', 'plant', 'play', 'player', 'point', 'police', 'policy',
             'political', 'politics', 'poor', 'popular', 'population', 'position',
             'positive', 'possible', 'power', 'practice', 'prepare', 'present',
             'president', 'pressure', 'pretty', 'prevent', 'price', 'private',
             'probably', 'problem', 'process', 'produce', 'product', 'production',
             'professional', 'professor', 'program', 'project', 'property', 'protect',
             'prove', 'provide', 'public', 'pull', 'purpose', 'push', 'put', 'quality',
             'question', 'quickly', 'quite', 'race', 'radio', 'raise', 'range', 'rate',
             'rather', 'reach', 'read', 'ready', 'real', 'reality', 'realize', 'really',
             'reason', 'receive', 'recent', 'recently', 'recognize', 'record', 'red', 'reduce',
             'reflect', 'region', 'relate', 'relationship', 'religious', 'remain', 'remember', 'remove',
             'report', 'represent', 'Republican', 'require', 'research', 'resource', 'respond', 'response',
             'responsibility', 'rest', 'result', 'return', 'reveal', 'rich', 'right', 'rise', 'risk', 'road',
             'rock', 'role', 'room', 'rule', 'run', 'safe', 'same', 'save', 'say', 'scene', 'school', 'science',
             'scientist', 'score', 'sea', 'season', 'seat', 'second', 'section', 'security', 'see', 'seek', 'seem',
             'sell', 'send', 'senior', 'sense', 'series', 'serious', 'serve', 'service', 'set', 'seven', 'several',
             'sex', 'sexual', 'shake', 'share', 'she', 'shoot', 'short', 'shot', 'should', 'shoulder', 'show', 'side',
             'sign', 'significant', 'similar', 'simple', 'simply', 'since', 'sing', 'single', 'sister', 'sit', 'site',
             'situation', 'six', 'size', 'skill', 'skin', 'small', 'smile', 'social', 'society', 'soldier', 'some',
             'somebody', 'someone', 'something', 'sometimes', 'son', 'song', 'soon', 'sort', 'sound', 'source',
             'south', 'southern', 'space', 'speak', 'special', 'specific', 'speech', 'spend', 'sport', 'spring',
             'staff', 'stage', 'stand', 'standard', 'star', 'start', 'state', 'statement', 'station', 'stay',
             'step', 'still', 'stock', 'stop', 'store', 'story', 'strategy', 'street', 'strong', 'structure',
             'student', 'study', 'stuff', 'style', 'subject', 'success', 'successful', 'such', 'suddenly',
             'suffer', 'suggest', 'summer', 'support', 'sure', 'surface', 'system', 'table', 'take', 'talk',
             'task', 'tax', 'teach', 'teacher', 'team', 'technology', 'television', 'tell', 'ten', 'tend',
             'term', 'test', 'than', 'thank', 'that', 'the', 'their', 'them', 'themselves', 'then', 'theory',
             'there', 'these', 'they', 'thing', 'think', 'third', 'this', 'those', 'though', 'thought', 'thousand',
             'threat', 'three', 'through', 'throughout', 'throw', 'thus', 'time', 'today', 'together', 'tonight',
             'too', 'top', 'total', 'tough', 'toward', 'town', 'trade', 'traditional', 'training', 'travel', 'treat',
             'treatment', 'tree', 'trial', 'trip', 'trouble', 'true', 'truth', 'try', 'turn', 'two', 'type', 'under',
             'understand', 'unit', 'until', 'upon', 'use', 'usually', 'value', 'various', 'very', 'victim', 'view',
             'violence', 'visit', 'voice', 'vote', 'wait', 'walk', 'wall', 'want', 'war', 'watch', 'water', 'way',
             'weapon', 'wear', 'week', 'weight', 'well', 'west', 'western', 'what', 'whatever', 'when', 'where',
             'whether', 'which', 'while', 'white', 'who', 'whole', 'whom', 'whose', 'why', 'wide', 'wife', 'will',
             'win', 'wind', 'window', 'wish', 'with', 'within', 'without', 'woman', 'wonder', 'word', 'work', 'worker',
             'world', 'worry', 'would', 'write', 'writer', 'wrong', 'yard', 'yeah', 'year', 'yes', 'yet', 'you', 'young',
             'your', 'yourself']


#Variables
_wins = 0 #To record wins
_losses = 0 #To record loss
tries = 0 #Player's tries (Set by the system)
difficulty = None #Player difficulty
_randomWordGenerated = "" #Random word will be set in this variable
wordClue = "" #Word clue will be set in this variable

#Function to clear things like some previous displays
def cls():
    os.system("cls")

#Function to display a Loading message
def loading(load_type):
    if load_type == 1:
        print("[*]=====================[ LOADING ]====================[*]")
        print("[*]                                                    [*]")
        print("                        LOADING...         ")
        print("[*]                                                    [*]")
        print("[*]====================================================[*]")
        return None
    elif load_type == 2:
        print("[*]=====================[ LOADING ]====================[*]")
        print("[*]                                                    [*]")
        print("                    GOING BACK TO MENU...         ")
        print("[*]                                                    [*]")
        print("[*]====================================================[*]")
        return None

#Function to prompt some error
def _promptError(err):

    if err == "numError":
        cls()
        print("[*]====================[ E R R O R ]===================[*]")
        print("[*]                                                    [*]")
        print("""       ERROR: The number you picked doesn't exist.
               Please pick again between 0 and 1.          """)
        print("[*]                                                    [*]")
        print("[*]====================================================[*]")
        sleep(2.5)
        cls()
        return None
    elif err == "valErr" or err == "typeErr":
        cls()
        print("[*]====================[ E R R O R ]===================[*]")
        print("[*]                                                    [*]")
        print("              ERROR: Please, Enter NUMBERS only.         ")
        print("[*]                                                    [*]")
        print("[*]====================================================[*]")
        sleep(2.5)
        cls()
        return None

# Generate a random word from the list of words.
def _randomWord():

    #Word lenght will be generated base on difficulty player picked.
    randomNum = random.randint(0,len(_wordList))

    if difficulty == 0 and len(_wordList[randomNum]) >= 6:
        _randomWord()
    elif difficulty == 1 and (len(_wordList[randomNum]) <= 5 and len(_wordList[randomNum])) >= 9:
        _randomWord()
    elif difficulty == 2 and len(_wordList[randomNum]) <= 8 :
        _randomWord()
    else:
        global _randomWordGenerated
        _randomWordGenerated = _wordList[randomNum]



#Function to generate a clue from a given word
def _wordClue():
    randomIndexes = [] #list of generated random numbers. This will be use to print the index of a given word for a clue. 
                       #For Example: the generated numbers in randomIndexes are [3,0,2] and the given word is "Hello" then the word clue will be "H_ll_".
                       
    clueWord = [] #Here will be the clue word will stored.

    #While loop is use to generate a random number for index.
    while len(randomIndexes) != int(len(_randomWordGenerated) / 2):
        randomNum = random.randint(0,len(_randomWordGenerated) - 1)
        if randomNum not in randomIndexes:
            randomIndexes.append(randomNum)
        
    #For loop is use to generate a clue word base on the given random generated number in the randomIndexes list.
    for loops in range(len(_randomWordGenerated)):
        if loops in randomIndexes:
            clueWord.append(f"{_randomWordGenerated[loops]} ")
        else:
            clueWord.append("_ ")
    return ''.join(map(str,clueWord))


#Function to set the game difficulty
def _difficulty():
        global difficulty, tries, wordClue
        cls()
        print("[*]====================[ DIFFICULTY ]===================[*]")
        print("[*]                                                     [*]")
        print("                     PICK A DIFFICULTY         ")
        print("[*]                                                     [*]")
        print("                        [0] - Easy               ")
        print("                        [1] - Medium                    ")
        print("                        [2] - Hard                   ")
        print("[*]                                                     [*]")
        print("                        [3] - Go Back       ")
        print("[*]                                                     [*]")
        print("[*]=====================================================[*]")

        try:
            _choose = int(input("Pick: "))
            if _choose == 0:
                cls()
                difficulty = 0
                _randomWord()
                wordClue = _wordClue()
                tries = 10
                cls()
                loading(1)
                sleep(1.5)
                _display()

            elif _choose == 1:
                cls()
                difficulty = 1
                _randomWord()
                wordClue = _wordClue()
                tries = 5
                cls()
                loading(1)
                sleep(1.5)
                _display()
            elif _choose == 2:
                cls()
                difficulty = 2
                _randomWord()
                cls()
                loading(1)
                wordClue = _wordClue()
                tries = 3
                sleep(1.5)
                _display()
            elif _choose == 3:
                cls()
                loading(2)
                sleep(1.5)
                cls()
                _start()
            else:
                _promptError("numError")
                _difficulty()
        except (ValueError, TypeError):
          _promptError("valErr")
          _difficulty()





#Function to verify the user's input and check if it is a correct guess.
def _verifyWord(word):
    global _wins, tries
    if word == _randomWordGenerated:
        cls()
        print("[*]======================[ W O N ]=====================[*]")
        print("[*]                                                    [*]")
        print("               YOU GUESSED IT RIGHT! YOU WON!         ")
        print("[*]                                                    [*]")
        print("[*]====================================================[*]")
        sleep(1.5)
        cls()
        loading(2)
        sleep(1.5)
        tries = 0
        _wins = _wins + 1
        _start()
    else:
        cls()
        print("[*]====================[ W R O N G ]===================[*]")
        print("[*]                                                    [*]")
        print("                   OOOPSS!!! WRONG GUESS         ")
        print("[*]                                                    [*]")
        print("[*]====================================================[*]")
        sleep(1.5)
        tries = tries - 1
        _display()
    return None

#In-game Display with Game Over Display aftermath.
def _display():
    global _losses
    cls()
    while tries != 0:
        print("[*]=================[ GUESS THE WORD ]=================[*]")
        print("[*]                                                    [*]")
        print(f"                Word lenght: {len(_randomWordGenerated)}")
        print(f"                  Word Clue: {wordClue}")
        print("[*]                                                    [*]")
        print("[*]====================================================[*]")
        print("[*]                                                    [*]")
        print(f"                 Tries left: {tries}\n")
        _userInput = input("                     Answer: ")
        _verifyWord(_userInput)
        return None
    
    cls()
    _losses = _losses + 1
    print("[*]====================[ GAME OVER ]===================[*]")
    print("[*]                                                    [*]")
    print("                       GAME OVER! :'(         ")
    print("[*]                                                    [*]")
    print("[*]====================================================[*]")
    sleep(2)
    cls()
    loading(1)
    sleep(1.5)
    _start()

#Function to start the program
def _start():
        cls()
        print("[*]====================================================[*]")
        print(f"              WINS: {_wins}               LOSSES: {_losses}         ")
        print("[*]====================================================[*]")
        print("[*]                                                    [*]")
        print("                       [0] - New Game")
        print("                       [1] - Exit")
        print("[*]                                                    [*]")
        print("[*]====================================================[*]")

        try:
            _choose = int(input("Pick: "))
            if _choose == 0:
                cls()
                sleep(0.5)
                loading(1)
                sleep(1.5)
                _difficulty()
            elif _choose == 1:
                cls()
                print("Exiting program...")
                sleep(1.5)
                cls()
                exit()
            else:
                _promptError("numError")
                _start()
        except (ValueError, TypeError):
            _promptError("valErr")
            _start()

#Start the program
_start()

