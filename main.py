from auto import App, Step

step_1 = Step((42, 126), '', True, 0.5, 'check_step_1.png')
step_2 = Step((0, 0), 'esc', False, 0.5, 'check_step_2.png')
step_3 = Step((42, 261), '', True, 0.5, 'check_step_3.png')

app = App((57, 204, 44, 22), '2222', step_1, step_2, step_3)

app.run()
