# task dealer program
import settings
import tasks


if __name__ == '__main__':
    
    DECKS = {}
    deckName = 'defaultDeck'
    DECKS[deckName] = tasks.TaskDeck(deckName)
    
    DEALERS = {}
    dealerName = 'defaultDealer'
    DEALERS[deckName] = tasks.TaskDealer(dealerName)

    while True:
        command = input().split(' ')
        if command[0] == 'q':
            break
        elif command[0] == 'dealers':
            for dealer in DEALERS:
                print(dealer)
        elif command[0] == 'decks':
            for deck in DECKS:
                print(deck)
        elif command[0] == 'deal':
            DEALERS[command[1]].deal()

        # elif command[0] in [d.name for d in DEALERS]:
        #     if command[1] == 'add':
        #         pass
        # elif command[0] in [d.name for d in DECKS]:
        #     print('its a deck')


        # elif command[0] == 'add':
        #     tasks.add_task(command[1])
        # elif command[0] == 'create':
        #     tasks.create_task(command[1])