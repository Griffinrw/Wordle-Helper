text_file = 'answers.txt'
f = open(text_file, 'r')
WORDLIST = f.readlines()
END = False
START_OVER = False







def request_parameters():

    '''1 not in [c in word.upper() for c in ['S', 'I', 'N', 'Q', 'U', 'B', 'R']]'''

    grey = request_grey()
    yellow = request_yellow()
    green = request_green()

    return grey, yellow, green

def request_grey():
    ### ask the user what letters AREN'T in the word

    grey_letters = input('Please input the letters that ARE NOT in the word (grey letters)\n Separate the letters with commas\nPlease enter "NA" if there are none')
    if grey_letters.upper() != 'NA':

        grey_letters = grey_letters.replace(' ', '')
        grey_list = grey_letters.split(',')

    else:
        grey_list = None
    return grey_list


def request_yellow():
    ### ask the user what letters are YELLOW and where
    yellow_letters = input('Please input the letters that are in the word and what location they were yellow,\n if E was yellow on the first slot enter it as E1\nPlease enter "NA" if there are none')
    if yellow_letters.upper() != 'NA':

        yellow_letters = yellow_letters.replace(' ', '')
        yellow_list = yellow_letters.split(',')
    else:
        yellow_list = None

    return yellow_list



def request_green():
    ### ask the user what letters are GREEN and where
    green_letters = input('Please input the letters are in the word and what location they were green,\n if E was green on the first slot enter it as E1\nPlease enter "NA" if there are none')
    if green_letters.upper() != 'NA':
        green_letters = green_letters.replace(' ', '')
        green_list = green_letters.split(',')
    else:
        green_list = None

    return green_list

def apply_parameters(grey_letters=None, yellow_letters=None, green_letters=None):
    global END
    viable_words = []

    ### make sure the words do not have any grey letters
    if grey_letters != None:
        for word in WORDLIST:
            if 1 not in [c in word.upper() for c in grey_letters]:
                viable_words.append(word)
    else:
        viable_words = WORDLIST



    new_list = []
    if yellow_letters != None:
        for word in viable_words:
            ### we receive a yellow word as a str denoting the letter and its position in the word, for example 'S1'
            ### we then separate that into two variables
            ### remove any words that don't have the letter at all
            ### then remove any words where the position of the letter matches the word exactly (in that case it would have been green, not yellow)
            word = word.upper()
            bool_list = []
            for yel in yellow_letters:
                letter = yel[0]
                i = int(yel[1])-1
                if letter in word and word[i] != letter:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
            if all(bool_list): ### checks to make sure that every yellow letter's requirements are accounted for and not just one
                new_list.append(word)
                    #new_list.append(word)
        viable_words = new_list


    ### make sure the words have the green letters AND they are in that exact position
    new_list = []
    if green_letters != None:
        for word in viable_words:
            word=word.upper()
            bool_list=[]
            for green in green_letters:
                letter = green[0]
                i = int(green[1])-1
                try:
                    if word[i] == letter:
                        bool_list.append(True)
                    else:
                        bool_list.append(False)
                        #new_list.append(word)
                except IndexError: # if there's an index error, that word def can't be viable
                    bool_list.append(False)
            if all(bool_list):
                new_list.append(word)
        viable_words = new_list
    printed_list = []
    for word in viable_words:
        printed_list.append(word.rstrip())

    print('')
    print('greys', grey_letters, 'yellows', yellow_letters, 'greens', green_letters)
    print('')
    print('Possible Answers:', printed_list)

    player_choice = input("Would you like to 'add more' information, 'start over', or 'quit'?")
    if player_choice == 'add more':
        run_program(grey_letters, yellow_letters, green_letters)
    elif player_choice == 'start over':
        run_program()
    elif player_choice == 'quit':
        END = True
    return viable_words


def run_program(og_grey=None, og_yellow=None, og_green=None):
    grey, yellow, green = request_parameters()
    if grey is not None and og_grey is not None:
        grey = og_grey+grey
    if grey is None and og_grey is not None:
        grey = og_grey


    if yellow is not None and og_yellow is not None:
        yellow = og_yellow+yellow
    if yellow is None and og_yellow is not None:
        yellow = og_yellow


    if green is not None and og_green is not None:
        green = og_green+green
    if green is None and og_green is not None:
        green = og_green


    apply_parameters(grey, yellow, green)


if __name__ == '__main__':
    while not END:
        run_program()

