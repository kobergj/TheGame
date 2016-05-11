import configuration.log_details as log

class PlayerInput:

    def __init__(self, player_choice, view_model):

        self.next_viewmodel = view_model.next

        self.change_func = 



    def __call__(self, player):
        # May be "True" is not the best option...
        while True:
            log.log('Awaiting View Model')
            view_model = self.viewmodel_queue.get()
            log.log('Awaiting Input')
            players_choice = self.view(view_model)
            # Lame
            if players_choice == 'I wanna quit the goddamn Game!':
                return
            log.log('Sending Update Func')
            update_func = view_model.get_func(players_choice)
            self.update_queue.put(update_func)

            log.log('Sending to V')
            self.choice_queue.put(players_choice)