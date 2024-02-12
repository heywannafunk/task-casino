# task dealer program
import settings
import tasks
import pickle


if __name__ == '__main__':
    
    DECKS = {}
    deckName = 'defaultDeck'
    DECKS[deckName] = tasks.TaskDeck(deckName)
    # create some sort of task creation without inputing the values
    DECKS[deckName].tasks.append(tasks.Task('testTask1', 0, 'testtasks.com', 0.0, False))
    # DECKS[deckName].add_task(tasks.Task('testTask2', 0, 'testtasks.com', 0.0, False))

    DEALERS = {}
    dealerName = 'defaultDealer'
    DEALERS[dealerName] = tasks.TaskDealer(dealerName)
    DEALERS[dealerName].decks.append(DECKS[deckName])    

    while True:
        command = input().split(' ')
        
        if command[0] == 'q':
            break

        # https://stackoverflow.com/questions/4529815/saving-an-object-data-persistence
        # nice stackoverflow thread about pickle saving
        if command[0] == 's':
            pickle.dump(DECKS, file=open('decks.pickle', "wb"))
            pickle.dump(DEALERS, file=open('dealers.pickle', "wb"))


        elif command[0] == 'dealers':
            if len(command) == 1:
                for dealer in DEALERS:
                    print(dealer)
            elif command[1] in DEALERS:
                print(DEALERS[command[1]].decks)


        elif command[0] == 'decks':
            if len(command) == 1:
                for deck in DECKS:
                    print(deck)
            elif command[1] in DECKS:
                deckName = command[1]
                if len(command) > 2:
                    if command[2] == 'tasks':
                        print(DECKS[deckName].tasks)
                    if command[2] == 'add':
                        DECKS[deckName].add_task()
                else:
                    print('command: decks <deckname> <command> \n   tasks: to see the tasks in the deck\n   add: add a task to a deck')


        elif command[0] == 'deal': # handle wrong commands
            DEALERS[command[1]].deal()


        elif command[0] == 'create': # handle wrong commands
            if command[1] == 'deck':
                # let user create a deck
                pass
            if command[1] == 'dealer':
                # let user create a dealer
                pass


        else:
            print('unknown command')