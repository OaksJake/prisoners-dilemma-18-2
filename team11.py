import random;
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Sozi' 
"""
Gender:	Masculine Type:	Adult 
Nationality:	Norwegian 
Location:	Norway 
Language:	Norwegian 
Life & Times Age:	50 
Birth date:	May 20, 1967 (10:37 AM)
Physical
Height:	171 cm / 5 ft 7 in
Weight:	74 kg / 162 lbs
Handedness:	Right
Blood type:	O+
Future Outlook
Death date:	September 3, 2052 (8:30 PM)
Lifespan:	85
Cause of death:	Unspecified Illness
"""


strategy_name = 'Betray'
strategy_description = 'Always betray, no matter what'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    
    '''
    #chooses to betray or collude based on random int
    number = random.randint(0,1)
    
    if number == 0:
        return 'c'
        
    else:
        return 'b'
    '''
    
    '''
    #always colludes
    return 'c'
    
    '''
    
    '''
    #Smart analysis
    for i in range(len(their_history)):
        if their_history[i] == 'b':
            betray +=1
        elif their_history[i] == 'c':
            collude +=1
            
        if collude > betray:
            return 'c'
        elif betray > collude:
            return 'b'
        
        return 'b'
    '''
    
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'b'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             