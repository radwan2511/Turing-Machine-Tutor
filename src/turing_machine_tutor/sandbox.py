import inspect
import os
import sys
# Add the parent directory of mypackage to the Python path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.Challenge import Challenge
from turing_machine_tutor.CombinedTuringMachine import CombinedTuringMachine
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.TuringMachineController import TuringMachineController
from turing_machine_tutor.Next import Next
from turing_machine_tutor.MultiNext import MultiNext
from turing_machine_tutor.IFTuringMachine import IFTuringMachine
from turing_machine_tutor.WhileTuringMachine import WhileTuringMachine
from turing_machine_tutor.ConcatenateTM import ConcatenateTM
from turing_machine_tutor.MultiTapeTuringMachine import MultiTapeTuringMachine
from turing_machine_tutor.Call_Turing_Machine import Call_Turing_Machine




# # def test_me(number):
# #     if number==1:
# #         return "one"
# #     if number==2:
# #         return "two"
# #     if number==3:
# #         return "three"
# #     return


# # ok=Next(1,2,3)
# # print(ok.try_me(test_me))



#
# emptyString = TuringMachine(
#     states={'q0', 'q1', 'rej', 'acc'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', '_'},
#     blank = '_',
#     transitions={
#         ('q0', '0'): Next('q1', '0', 'R'),
#         ('q0', '1'): Next('q1', '1', 'R'),
#         ('q1', '0'): Next('q0', '0', 'R'),
#         ('q1', '1'): Next('q0', '1', 'R'),
#         ('q0', '_'): Next('acc', '_', 'R'),
#         ('q1', '_'): Next('rej', '_', 'R'),
#     },
#     initial_state='q0',
#     accept_states={'acc'},
#     reject_states={'rej'}
# )


# Create a Turing machine
# tm1 = TuringMachine(
#     states={'q0', 'q1', 'q2', 'q3'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): Next('q1', '0', 'R'),
#         ('q0', '1'): Next('q1', '1', 'R'),
#         ('q1', '0'): Next('q0', '0', 'R'),
#         ('q1', '1'): Next('q0', '1', 'R'),
#         ('q0', 'B'): Next('q3', 'B', 'R'),
#         ('q1', 'B'): Next('q2', 'B', 'R'),
#     },
#     initial_state='q0',
#     accept_states={'q3'},
#     reject_states={'q2'}
# )

# anbn_turing_machine = TuringMachine(
#     states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): Next('q1', 'X', 'R'),  # Move right and replace 0 with X
#         ('q1', '0'): Next('q1', '0', 'R'),  # Continue moving right over 0
#         ('q1', 'Y'): Next('q1', 'Y', 'R'),  # Skip Y
#         ('q1', '1'): Next('q2', 'Y', 'L'),  # Move left and replace 1 with Y
#         ('q2', 'Y'): Next('q2', 'Y', 'L'),  # Continue moving left over Y
#         ('q2', '0'): Next('q2', '0', 'L'),  # Continue moving left over 0
#         ('q2', 'X'): Next('q0', 'X', 'R'),  # Move right to find the Next 0 after 1s
#         ('q0', 'Y'): Next('q0', 'Y', 'R'),  # Skip Y in the process
#         ('q0', 'B'): Next('q4', 'B', 'R'),   # Accept if B is encountered after checking
#         ('q0', '1'): Next('q5', 'B', 'R'),
#         ('q1', 'B'): Next('q5', 'B', 'L')
#     },
#     initial_state='q0',
#     accept_states={'q4'},
#     reject_states={'q5'}
# )


# controller = TuringMachineController()
# # controller.add_turing_machine('emptyString', emptyString)
# # controller.add_turing_machine('tm1',tm1)
# controller.add_turing_machine('0n1n',anbn_turing_machine)

# # # # Run the Turing machine from the library
# # # mrs= controller.run_turing_machine('tm1', '000111')
# # # print(tm1.given_state_is_in_acceptance(mrs.state))
# # # mrs= controller.run_turing_machine('0n1n', '0000011111')
# # # print(anbn_turing_machine.given_state_is_in_acceptance(mrs.state))


# def is_0n1n(s):
#     if(len(s) < 2):
#         return False
#     elif(len(s) == 2 and s != "01"):
#         return False
#     elif(len(s) == 2 and s == "01"):
#         return True
#     st = s.split('01')
#     if(len(st) != 2):
#         return False
#     if(len(st[0]) != len(st[1])):
#         return False
#     for i in st[0]:
#         if i != '0':
#             return False
#     for i in st[1]:
#         if i != '1':
#             return False
#     return True

# #
controller = TuringMachineController()


tm_challenge2 = MultiTapeTuringMachine(
    states={'qs', 'q1', 'q2','q3', 'qa'},
    input_alphabet={'1'},
    tape_alphabet={'1', 'X','B'},
    transition_function={
    ('qs', '1', 'B'): MultiNext('q1', '1', '1', 'R','R'),
    ('qs', 'B','B'): MultiNext('qa', 'B', 'B', 'S','S'),
    ('q1', '1','B'): MultiNext('q2', 'X', 'B', 'R', 'S'),
    ('q1', 'B','B'): MultiNext('q3', 'B', 'B', 'S', 'L'),
    ('q2', '1', 'B'): MultiNext('q1', '1', '1', 'R', 'R'),
    ('q2', 'B','B'): MultiNext('qa', 'B', 'B', 'S', 'S'),
    ('q3', 'B','1'): MultiNext('qa', 'B', 'B', 'S', 'R')
    },
    start_state='qs',
    accept_state={'qa'},
    reject_state={},
    num_tapes=2
)

controller.add_turing_machine("DivideByTwo",tm_challenge2)


tm_challenge3 = MultiTapeTuringMachine(
    states={'qs', 'q1', 'q2','qr', 'qacc'},
    input_alphabet={'1'},
    tape_alphabet={'1', 'X','S', 'B'},
    transition_function={
    ('qs', '1', 'B'): Call_Turing_Machine("DivideByTwo", tm_challenge2, [0], 'q1', 'qr'),
    ('q1', '1', 'B'): MultiNext('qs', '1', '1', 'S', 'R'),
    ('q1', 'B', 'B'): MultiNext('qacc', 'B', 'B', 'S', 'S'),
    ('q1', 'B', '1'): MultiNext('q1', 'B', '1', 'S', 'R')
    },
    start_state='qs',
    accept_state={'qacc'},
    reject_state={'qr'},
    num_tapes=2
)
controller.add_turing_machine("LogBaseTwo",tm_challenge3)

controller.visualize_step_by_step ("LogBaseTwo", "11111111")
print("shit")

#controller.add_challenge("0n1n",{'a'},"turing machine that accepts 0n1n",is_0n1n,{"0011","01"});
# controller.collect_machines_and_challenges()

# controller.add_challenge("random_shit","turing machine that accepts 0n1n",is_0n1n,{"0011","01"});
# controller.add_challenge("random_shit_2","turing machine that accepts 0n1n",is_0n1n,{"0011","01"});
# controller.get_challenges()
# # controller.validate_turing_machine('0n1n',is_0n1n,{"0011"})
# # # controller.visualize('0n1n',"01")
# # # controller.visualize_step_by_step('0n1n',"01")





# step1 = TuringMachine(
#     states={'q0', 'q1', 'q2','q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): Next('q2', 'X', 'R'),  # Step 1 change 0 to X
#         ('q0', '1'): Next('q3', '1', 'S'),
#         ('q0', 'X'): Next('q3', 'X', 'S'),
#         ('q0', 'Y'): Next('q3', 'Y', 'S'),
#         ('q0', 'B'): Next('q3', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )

# step2 = TuringMachine(
#     states={'q0', 'q1', 'q2','q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): Next('q0', '0', 'R'),  # Step 2 move right to the first 1
#         ('q0', '1'): Next('q2', '1', 'S'),  # if you do not find symbol 1, reject the language
#         ('q0', 'X'): Next('q0', 'X', 'R'),
#         ('q0', 'Y'): Next('q0', 'Y', 'R'),
#         ('q0', 'B'): Next('q3', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )

# step3 = TuringMachine(
#     states={'q0', 'q1', 'q2','q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): Next('q3', '0', 'S'),  # Step 3 change 1 to Y
#         ('q0', '1'): Next('q2', 'Y', 'L'),
#         ('q0', 'X'): Next('q3', 'X', 'S'),
#         ('q0', 'Y'): Next('q3', 'Y', 'S'),
#         ('q0', 'B'): Next('q3', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )

# step4 = TuringMachine(
#     states={'q0', 'q1', 'q2','q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): Next('q0', '0', 'L'),  # Step 4 Move Left to Leftmost 0
#         ('q0', '1'): Next('q3', '1', 'S'),
#         ('q0', 'X'): Next('q2', 'X', 'R'),
#         ('q0', 'Y'): Next('q0', 'Y', 'L'),
#         ('q0', 'B'): Next('q3', 'B', 'R')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )

# #step 5 repeat steps number 01 to 04 until no more 0 and 1 remain in the input tape
# step5 = TuringMachine(
#     states={'q0', 'q1', 'q2','q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): Next('q2', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
#         ('q0', '1'): Next('q2', '1', 'S'),
#         ('q0', 'X'): Next('q0', 'X', 'R'),
#         ('q0', 'Y'): Next('q0', 'Y', 'R'),
#         ('q0', 'B'): Next('q3', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )
# step6 = TuringMachine(
#     states={'q0', 'q1', 'q2','q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): Next('q3', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
#         ('q0', '1'): Next('q3', '1', 'S'),
#         ('q0', 'X'): Next('q0', 'X', 'R'),
#         ('q0', 'Y'): Next('q0', 'Y', 'R'),
#         ('q0', 'B'): Next('q2', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )

# combined_tm = CombinedTuringMachine({'0', '1', 'X', 'Y', 'B'})
# combined_tm.add('step1', step1)
# combined_tm.add('step2', step2)
# combined_tm.add('step3', step3)
# combined_tm.add('step4', step4)
# combined_tm.setTuringMachineWhileCondition("myCond",step5)
# controller.add_turing_machine('combined_shit',combined_tm)

# # # #----------------------------testing combine_tm_with_conidition---------------------------

# controller.validate_turing_machine('combined_shit',is_0n1n,{"0011"})
# mrs=controller.run_turing_machine('combined_shit',"0011")
# mrs=controller.run_turing_machine('combined_shit', "0011")
# print("at end tape is:  ",mrs.tape)

# print(step6.given_state_is_in_acceptance(step6.run(mrs.tape.copy()).state))
# controller.visualize('combined_shit', "0011")
# controller.submit()

# # #----------------------------------------------------------------------------------------


# #to do: DONE

# #controller.visualize_step_by_step('combined_shit', "0011")





# # #----------------------------testing combine_tm------------------------------------------

# # #mrs= controller.run_turing_machine('combined_shit','01')

# # # print("fuck you is:   ",combined_tm.turing_machines[-1].given_state_is_in_acceptance(mrs.state))
# # # controller.validate_turing_machine('combined_shit',is_0n1n,{"0011"})
# # # controller.visualize('combined_shit',"01")
# # #controller.visualize_combined_machine_step_by_step('combined_shit',"01")

# # #----------------------------------------------------------------------------------------


# # #--------------------------If Turing machine----------------------------------------------
# ifTm = TuringMachine( # condition if input legth is less than 4 accept else reject
#     states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): Next('q1', '0', 'R'),  
#         ('q0', '1'): Next('q1', '1', 'R'),

#         ('q1', '0'): Next('q2', '0', 'R'),
#         ('q1', '1'): Next('q2', '1', 'R'),

#         ('q2', '0'): Next('q3', '0', 'R'),  
#         ('q2', '1'): Next('q3', '0', 'R'),
        
#         ('q3', '0'): Next('q6', '0', 'R'),
#         ('q3', '1'): Next('q6', '1', 'R'),
#         ('q3', 'B'): Next('q5', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q5'},
#     reject_states={'q6'}
# )

# #ifTm.run("01")

# # controller = TuringMachineController()
# # controller.add_turing_machine("if", ifTm)
# # mrs =  controller.run_turing_machine("if", "010")
# # print(mrs.tape)
# # print(ifTm.given_state_is_in_acceptance(mrs.state))

# thenTm = TuringMachine( # condition if input legth is less than 4 change every 1 to 0
#     states={'q0', 'q1', 'q2'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): Next('q0', '0', 'R'),  
#         ('q0', '1'): Next('q0', '0', 'R'),
#         ('q0', 'B'): Next('q1', 'B', 'R')
#     },
#     initial_state='q0',
#     accept_states={'q1'},
#     reject_states={'q2'}
# )

# elseTm = TuringMachine( # condition if input legth is less than 4 change every 0 to 1
#     states={'q0', 'q1', 'q2'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): Next('q0', '1', 'R'),  
#         ('q0', '1'): Next('q0', '1', 'R'),
#         ('q0', 'B'): Next('q1', 'B', 'R')
#     },
#     initial_state='q0',
#     accept_states={'q1'},
#     reject_states={'q2'}
# )

# if1 = IFTuringMachine()
# if1.setIfTM(ifTm,"if1")
# if1.setThenTM(thenTm,"then1")
# if1.setElseTM(elseTm, "else1")

# controller = TuringMachineController()
# # controller.add_turing_machine("if", if1)
# # mrs =  controller.run_turing_machine("if", "011")
# # print(mrs.tape)
# # print(ifTm.given_state_is_in_acceptance(mrs.state))

# #controller.visualize_step_by_step("if", "01111111")

# simple_turing_machine = TuringMachine(
#     states={'q0', 'q1','q2'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): Next('q1', '1', 'R'),  # if encountered 0 put 1 and move right
#         ('q0', '1'): Next('q0', '1', 'R'),  # if encountered 1 just move right
#         ('q0', 'B'): Next('q1', 'B', 'S'),  # if encountered 1 just move right
#         ('q1', '0'): Next('q1', '0', 'S'),  # after reaching q1 don't do anything
#         ('q1', '1'): Next('q1', '1', 'S'),  # after reaching q1 don't do anything
#         ('q1', 'B'): Next('q1', 'B', 'S'),  # after reaching q1 don't do anything

#     },
#     initial_state='q0',
#     accept_states={'q1'},
#     reject_states={'q2'}
# )


# simple_turing_machine_2 = TuringMachine(
#     states={'q0', 'q1','q2'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): Next('q0', '0', 'R'),  # if encountered 0 put 1 and move right
#         ('q0', '1'): Next('q1', '0', 'R'),  # if encountered 1 just move right
#         ('q0', 'B'): Next('q1', 'B', 'S'),  # if encountered 1 just move right
#         ('q1', '0'): Next('q1', '0', 'S'),  # after reaching q1 don't do anything
#         ('q1', '1'): Next('q1', '1', 'S'),  # after reaching q1 don't do anything
#         ('q1', 'B'): Next('q1', 'B', 'S'),  # after reaching q1 don't do anything

#     },
#     initial_state='q0',
#     accept_states={'q1'},
#     reject_states={'q2'}
# )


# while_machine = TuringMachine(
#     states={'q0', 'q1','q2'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): Next('q0', '0', 'R'),  # if encountered 0 put 1 and move right
#         ('q0', '1'): Next('q0', '1', 'R'),  # if encountered 1 just move right
#         ('q0', 'B'): Next('q1', 'B', 'S'),  # if encountered 1 just move right
#     },
#     initial_state='q0',
#     accept_states={'q1'},
#     reject_states={'q2'}
# )


# ifcond_machine= TuringMachine( ## if first letter is 1
#     states={'q0', 'q1','q2'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): Next('q2', '0', 'S'),
#         ('q0', '1'): Next('q1', '1', 'R'),
#         ('q0', 'B'): Next('q2', 'B', 'S'),

#     },
#     initial_state='q0',
#     accept_states={'q1'},
#     reject_states={'q2'}
# )


# combined_tm = CombinedTuringMachine()
# combined_tm.setTuringMachineWhileCondition(while_machine,"condition")
# combined_tm.add("step1",simple_turing_machine)
# combined_tm.add("step2",simple_turing_machine_2)

# controller.add_turing_machine("shit",simple_turing_machine)
# controller.add_turing_machine("shit2",combined_tm)


# if_machine=IFTuringMachine() #if first letter is 1 then convert first 0 to 1 else convert first 1 to 0

# if_machine.setIfTM(ifcond_machine,"ifcond")
# if_machine.setThenTM(simple_turing_machine,"convert_0_to_1")
# if_machine.setElseTM(simple_turing_machine_2,"convert_1_to_0")

# controller.add_turing_machine("ifshit",if_machine)

# controller.visualize("ifshit","10")



########################################################################################
# step1 = TuringMachine(
#             states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
#             input_alphabet={'0', '1'},
#             tape_symbols={'0', '1', 'X', 'Y', 'B'},
#             transitions={
#                 ('q0', '0'): Next('q1', 'X', 'R'),  # Step 1 change 0 to X
#                 ('q0', 'Y'): Next('q3', 'Y', 'R'),
#                 ('q1', '0'): Next('q1', '0', 'R'),
#                 ('q1', '1'): Next('q2', 'Y', 'L'),
#                 ('q1', 'Y'): Next('q1', 'Y', 'R'),
#                 ('q2', '0'): Next('q2', '0', 'L'),
#                 ('q2', 'X'): Next('q0', 'X', 'R'),
#                 ('q2', 'Y'): Next('q2', 'Y', 'L'),
#                 ('q3', 'Y'): Next('q3', 'Y', 'R'),
#                 ('q3', 'B'): Next('q4', 'B', 'L')
#             },
#             initial_state='q0',
#             accept_states={'q4'},
#             reject_states={'q5'}
#         )

# combined_tm = CombinedTuringMachine({'0', '1'})
# combined_tm.add('an_bn', step1)
# result = TuringMachineController()
# result.add_turing_machine("myCombined", combined_tm)

# def is_0n1n(s):
#     if(len(s) < 2):
#         return False
#     elif(len(s) == 2 and s != "01"):
#         return False
#     elif(len(s) == 2 and s == "01"):
#         return True
#     st = s.split('01')
#     if(len(st) != 2):
#         return False
#     if(len(st[0]) != len(st[1])):
#         return False
#     for i in st[0]:
#         if i != '0':
#             return False
#     for i in st[1]:
#         if i != '1':
#             return False
#     return True

#     return not stack  # Check if the stack is empty at the end
# def notValidFunc(asd):
#     return True

# res = result.validate_turing_machine("myCombined",is_0n1n)
# #self.assertEqual(res,True)
# print(res)
# #print(result.run_turing_machine("myCombined", "01"))
# #res = result.validate_turing_machine("myCombined",notValidFunc)
# #self.assertEqual(res,False)


# try:
#     step1 = TuringMachine(
#         states={'q0', 'q1', 'q2', 'q3'},
#         input_alphabet={'0', '1', 'X', 'Y', 'B'},
#         tape_symbols={'0', '1', 'X', 'Y', 'B'},
#         transitions={
#             ('q0', '0'): Next('q2', 'X', 'R'),  # Step 1 change 0 to X
#             ('q0', '1'): Next('q3', '1', 'S'),
#             ('q0', 'X'): Next('q3', 'X', 'S'),
#             ('q0', 'Y'): Next('q3', 'Y', 'S'),
#             ('q0', 'B'): Next('q3', 'B', 'S')
#         },
#         initial_state='q0',
#         accept_states={'q2'},
#         reject_states={'q3'}
#     )
#     step2 = TuringMachine(
#     states={'q0', 'q1', 'q2', 'q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): Next('q0', '0', 'R'),  # Step 2 move right to the first 1
#         ('q0', '1'): Next('q2', '1', 'S'),  # if you do not find symbol 1, reject the language
#         ('q0', 'X'): Next('q0', 'X', 'R'),
#         ('q0', 'Y'): Next('q0', 'Y', 'R'),
#         ('q0', 'B'): Next('q3', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )

#     step3 = TuringMachine(
#         states={'q0', 'q1', 'q2', 'q3'},
#         input_alphabet={'0', '1', 'X', 'Y', 'B'},
#         tape_symbols={'0', '1', 'X', 'Y', 'B'},
#         transitions={
#             ('q0', '0'): Next('q3', '0', 'S'),  # Step 3 change 1 to Y
#             ('q0', '1'): Next('q2', 'Y', 'L'),
#             ('q0', 'X'): Next('q3', 'X', 'S'),
#             ('q0', 'Y'): Next('q3', 'Y', 'S'),
#             ('q0', 'B'): Next('q3', 'B', 'S')
#         },
#         initial_state='q0',
#         accept_states={'q2'},
#         reject_states={'q3'}
#     )

#     step4 = TuringMachine(
#         states={'q0', 'q1', 'q2', 'q3'},
#         input_alphabet={'0', '1', 'X', 'Y', 'B'},
#         tape_symbols={'0', '1', 'X', 'Y', 'B'},
#         transitions={
#             ('q0', '0'): Next('q0', '0', 'L'),  # Step 4 Move Left to Leftmost 0
#             ('q0', '1'): Next('q3', '1', 'S'),
#             ('q0', 'X'): Next('q2', 'X', 'R'),
#             ('q0', 'Y'): Next('q0', 'Y', 'L'),
#             ('q0', 'B'): Next('q3', 'B', 'R')
#         },
#         initial_state='q0',
#         accept_states={'q2'},
#         reject_states={'q3'}
#     )

#     #step 5 repeat steps number 01 to 04 until no more 0 and 1 remain in the input tape
#     step5 = TuringMachine(
#         states={'q0', 'q1', 'q2', 'q3'},
#         input_alphabet={'0', '1', 'X', 'Y', 'B'},
#         tape_symbols={'0', '1', 'X', 'Y', 'B'},
#         transitions={
#             ('q0', '0'): Next('q2', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
#             ('q0', '1'): Next('q2', '1', 'S'),
#             ('q0', 'X'): Next('q0', 'X', 'R'),
#             ('q0', 'Y'): Next('q0', 'Y', 'R'),
#             ('q0', 'B'): Next('q3', 'B', 'S')
#         },
#         initial_state='q0',
#         accept_states={'q2'},
#         reject_states={'q3'}
#     )
#     step6 = TuringMachine(
#         states={'q0', 'q1', 'q2', 'q3'},
#         input_alphabet={'0', '1', 'X', 'Y', 'B'},
#         tape_symbols={'0', '1', 'X', 'Y', 'B'},
#         transitions={
#             ('q0', '0'): Next('q3', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
#             ('q0', '1'): Next('q3', '1', 'S'),
#             ('q0', 'X'): Next('q0', 'X', 'R'),
#             ('q0', 'Y'): Next('q0', 'Y', 'R'),
#             ('q0', 'B'): Next('q2', 'B', 'S')
#         },
#         initial_state='q0',
#         accept_states={'q2'},
#         reject_states={'q3'}
#     )

#     combined_tm = CombinedTuringMachine({'0', '1'})
#     combined_tm.add('Change 0 to X', step1)
#     combined_tm.add('Move Right To First 1', step2)
#     combined_tm.add('Change 1 to Y', step3)
#     combined_tm.add('Move Left to Leftmost 0', step4)
#     # test without cond
#     result = TuringMachineController()
#     result.add_turing_machine("myCombined", combined_tm)
#     res = result.run_turing_machine("myCombined", "0011")
#     print(res)
#     res = ''.join(res.tape)
#     res = res.replace('B','')
#     # test with while cond
#     result.remove("myCombined")
#     combined_tm.setTuringMachineWhileCondition("0 or 1 in tape", step5)
#     result.add_turing_machine("myCombined", combined_tm)
#     res = result.run_turing_machine("myCombined", "0011")
#     res = ''.join(res.tape)
#     res = res.replace('B','')
#     #self.assertEqual(result, "XXYY")
# except Exception as e:
#     print("NO")






# # language 0^n_1^n_2_0^n_1^n
# step1 = TuringMachine( 
#             states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
#             input_alphabet={'0', '1', '2', 'X', 'Y', 'B','Z'},
#             tape_symbols={'0', '1', '2', 'X', 'Y', 'B','Z'},
#             transitions={
#                 ('q0', '0'): Next('q1', 'X', 'R'),  # Step 1 change 0 to X
#                 ('q0', 'Y'): Next('q3', 'Y', 'R'),
#                 ('q1', '0'): Next('q1', '0', 'R'),
#                 ('q1', '1'): Next('q2', 'Y', 'L'),
#                 ('q1', 'Y'): Next('q1', 'Y', 'R'),
#                 ('q2', '0'): Next('q2', '0', 'L'),
#                 ('q2', 'X'): Next('q0', 'X', 'R'),
#                 ('q2', 'Y'): Next('q2', 'Y', 'L'),
#                 ('q3', 'Y'): Next('q3', 'Y', 'R'),
#                 ('q3', 'B'): Next('q4', 'B', 'S'),

#                 ('q3', '2'): Next('q4', '2', 'S')
#             },
#             initial_state='q0',
#             accept_states={'q4'},
#             reject_states={'q5'}
#         )
# cond = TuringMachine( #current head pos equals 0
#             states={'q0', 'q1', 'q2', 'q3'},
#             input_alphabet={'0', '1','2' , 'X', 'Y', 'B','Z'},
#             tape_symbols={'0', '1','2', 'X', 'Y', 'B','Z'},
#             transitions={
#                 ('q0', 'X'): Next('q0', 'X', 'R'),
#                 ('q0', 'Y'): Next('q0', 'Y', 'R'),
#                 ('q0', '2'): Next('q2', 'Z', 'R'),
#                 ('q0', 'Z'): Next('q0', 'Z', 'R')
#             },
#             initial_state='q0',
#             accept_states={'q2'},
#             reject_states={'q3'}
#         )

# combined_tm = CombinedTuringMachine({'0', '1', '2'})
# combined_tm.add('find_a_n_b_n', step1)
# #combined_tm.add('Move Left to Leftmost 0', step4)

# #you want to repeat steps number 01 to 04 until no more 0 and 1 remain in the input tape
# combined_tm.setTuringMachineWhileCondition("2 still in tape", cond)
# controller = TuringMachineController()
# ####################important step!!!! dont forget!!!##########################
# controller.add_turing_machine('OccurenceOf0==1',combined_tm)
# ###############################################################################

# controller.run_turing_machine('OccurenceOf0==1', "01201")

# # def check_zeros_equal_ones(input_str):
# #     if(len(input_str) == 0):
# #       return False
# #     if(str(input_str[0]) != "0"):
# #         return False
# #     count_0 = input_str.count('0')
# #     count_1 = input_str.count('1')
# #     return count_0 == count_1

# # controller.validate_turing_machine('OccurenceOf0==1', check_zeros_equal_ones)

##########################################################################




# function_string='''def is_wDw(txt):
#   l = len(txt)
#   if l%2 == 0:
#       return False
#   h = l//2
#   for i in range(l):
#       if i == h:
#           if txt[i] != '$':
#             return  False
#       elif txt[i] != 'a' and txt[i] != 'b':
#             return False
#   left=txt[:h]
#   right=txt[h+1:]
#   if left==right:
#     return True
#   else:
#     return False'''
# # Given string representation of TuringMachine
# tm_string = '''TuringMachine(
#     states={'q3', 'q8', 'q10', 'q5', 'q7', 'q9', 'q0', 'q2', 'q11', 'q6', 'q1', 'q4'},
#     input_alphabet={'a', '$', 'b'},
#     tape_symbols={'$', 'b', 'B', 'a', 'E'},
#     transitions={
#         ('q0', 'a'): Next('q3', 'E', 'R'),
#         ('q0', 'b'): Next('q4', 'E', 'R'),
#         ('q0', 'B'): Next('q2', 'B', 'S'),
#         ('q0', '$'): Next('q11', '$', 'R'),
#         ('q0', 'E'): Next('q2', 'E', 'S'),
#         ('q3', 'a'): Next('q3', 'a', 'R'),
#         ('q3', 'b'): Next('q3', 'b', 'R'),
#         ('q3', 'B'): Next('q2', 'B', 'S'),
#         ('q3', '$'): Next('q5', '$', 'R'),
#         ('q3', 'E'): Next('q2', 'E', 'R'),
#         ('q5', 'a'): Next('q7', 'E', 'S'),
#         ('q5', 'b'): Next('q2', 'b', 'S'),
#         ('q5', 'B'): Next('q2', 'B', 'S'),
#         ('q5', '$'): Next('q2', '$', 'R'),
#         ('q5', 'E'): Next('q5', 'E', 'R'),
#         ('q7', 'a'): Next('q2', 'b', 'S'),
#         ('q7', 'b'): Next('q2', 'b', 'S'),
#         ('q7', 'B'): Next('q2', 'B', 'S'),
#         ('q7', '$'): Next('q9', '$', 'L'),
#         ('q7', 'E'): Next('q7', 'E', 'L'),
#         ('q9', 'a'): Next('q9', 'a', 'L'),
#         ('q9', 'b'): Next('q9', 'b', 'L'),
#         ('q9', 'B'): Next('q2', 'B', 'S'),
#         ('q9', '$'): Next('q9', '$', 'L'),
#         ('q9', 'E'): Next('q0', 'E', 'R'),
#         ('q11', 'a'): Next('q2', 'b', 'S'),
#         ('q11', 'b'): Next('q2', 'b', 'S'),
#         ('q11', 'B'): Next('q1', 'B', 'S'),
#         ('q11', '$'): Next('q2', '$', 'L'),
#         ('q11', 'E'): Next('q11', 'E', 'R'),
#         ('q4', 'a'): Next('q4', 'a', 'R'),
#         ('q4', 'b'): Next('q4', 'b', 'R'),
#         ('q4', 'B'): Next('q2', 'B', 'S'),
#         ('q4', '$'): Next('q6', '$', 'R'),
#         ('q4', 'E'): Next('q2', 'E', 'R'),
#         ('q6', 'a'): Next('q2', 'a', 'S'),
#         ('q6', 'b'): Next('q8', 'E', 'S'),
#         ('q6', 'B'): Next('q2', 'B', 'S'),
#         ('q6', '$'): Next('q2', '$', 'R'),
#         ('q6', 'E'): Next('q6', 'E', 'R'),
#         ('q8', 'a'): Next('q2', 'b', 'S'),
#         ('q8', 'b'): Next('q2', 'b', 'S'),
#         ('q8', 'B'): Next('q2', 'B', 'S'),
#         ('q8', '$'): Next('q10', '$', 'L'),
#         ('q8', 'E'): Next('q8', 'E', 'L'),
#         ('q10', 'a'): Next('q10', 'a', 'L'),
#         ('q10', 'b'): Next('q10', 'b', 'L'),
#         ('q10', 'B'): Next('q2', 'B', 'S'),
#         ('q10', '$'): Next('q10', '$', 'L'),
#         ('q10', 'E'): Next('q0', 'E', 'R')
#     },
#     initial_state='q0',
#     accept_states={'q1'},
#     reject_states={'q2'}
# )'''



# tm_object = eval(tm_string)
# ok=tm_object.run("ab$ab")
# exec(function_string)

# function_name = controller.extract_func_name(function_string)
# function_object = globals()[function_name]

# print(is_wDw("ab$ab"))
# ok=Challenge("d",{"d"},"d",function_object,{'a'},function_string)

# print(69)

# ifTm = TuringMachine(  # condition if input legth is less than 4 accept else reject
#         states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
#         input_alphabet={'0', '1'},
#         tape_symbols={'0', '1', 'B'},
#         transitions={
#             ('q0', '0'): Next('q1', '0', 'R'),
#             ('q1', '1'): Next('q3', '1', 'R'),
#             ('q3', 'B'): Next('q3', 'B', 'L'),
#             ('q3', '1'): Next('q3', '1', 'L'),
#             ('q3', '0'): Next('q3', '0', 'L'),
#         },
#         initial_state='q0',
#         accept_states={'q5'},
#         reject_states={'q6'}
#     )

# controller.add_turing_machine("shit",ifTm)
# controller.visualize("shit","01")

# def is_0n1n(s):
#     if(len(s) < 2):
#         return False
#     elif(len(s) == 2 and s != "01"):
#         return False
#     elif(len(s) == 2 and s == "01"):
#         return True
#     st = s.split('01')
#     if(len(st) != 2):
#         return False
#     if(len(st[0]) != len(st[1])):
#         return False
#     for i in st[0]:
#         if i != '0':
#             return False
#     for i in st[1]:
#         if i != '1':
#             return False
#     return True

# controller.add_challenge("0n1n","turing machine that accepts 0n1n",is_0n1n,{"02","01"});

# controller.get_challenges()


##########################################################################


# # language 0^n_1^n_2_0^n_1^n (2_0^n_1^n_2_0^n_1^n)*
# step1 = TuringMachine(
#             states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
#             input_alphabet={'0', '1', '2', 'X', 'Y', 'B','Z'},
#             tape_symbols={'0', '1', '2', 'X', 'Y', 'B','Z'},
#             transitions={
#                 ('q0', '0'): Next('q1', 'X', 'R'),  # Step 1 change 0 to X
#                 ('q0', 'Y'): Next('q3', 'Y', 'R'),
#                 ('q1', '0'): Next('q1', '0', 'R'),
#                 ('q1', '1'): Next('q2', 'Y', 'L'),
#                 ('q1', 'Y'): Next('q1', 'Y', 'R'),
#                 ('q2', '0'): Next('q2', '0', 'L'),
#                 ('q2', 'X'): Next('q0', 'X', 'R'),
#                 ('q2', 'Y'): Next('q2', 'Y', 'L'),
#                 ('q3', 'Y'): Next('q3', 'Y', 'R'),
#                 ('q3', 'B'): Next('q4', 'B', 'S'),

#                 ('q3', '2'): Next('q4', '2', 'S')
#             },
#             initial_state='q0',
#             accept_states={'q4'},
#             reject_states={'q5'}
#         )
# cond = TuringMachine( #current head pos equals 0
#             states={'q0', 'q1', 'q2', 'q3'},
#             input_alphabet={'0', '1','2' , 'X', 'Y', 'B','Z'},
#             tape_symbols={'0', '1','2', 'X', 'Y', 'B','Z'},
#             transitions={
#                 ('q0', 'X'): Next('q0', 'X', 'R'),
#                 ('q0', 'Y'): Next('q0', 'Y', 'R'),
#                 ('q0', '2'): Next('q2', 'Z', 'R'),
#                 ('q0', 'Z'): Next('q0', 'Z', 'R')
#             },
#             initial_state='q0',
#             accept_states={'q2'},
#             reject_states={'q3'}
#         )
# combined_tm = CombinedTuringMachine({'0', '1', '2'})
# combined_tm.add('find_a_n_b_n', step1)
# #combined_tm.add('Move Left to Leftmost 0', step4)

# #you want to repeat steps number 01 until no more 2 remain in the tape
# combined_tm.setTuringMachineWhileCondition("2 still in tape", cond)
# ####################important step!!!! dont forget!!!##########################
# controller.add_turing_machine('WhileCombined',combined_tm)


# #controller.run_turing_machine('WhileCombined', "001120011")

# controller.visualize('WhileCombined',"01201")
# def is_0n1n(s):
#     if(len(s) < 2):
#         return False
#     elif(len(s) == 2 and s != "01"):
#         return False
#     elif(len(s) == 2 and s == "01"):
#         return True
#     st = s.split('01')
#     if(len(st) != 2):
#         return False
#     if(len(st[0]) != len(st[1])):
#         return False
#     for i in st[0]:
#         if i != '0':
#             return False
#     for i in st[1]:
#         if i != '1':
#             return False
#     return True

# controller.add_challenge("0n1n", {'0','1'},"turing machine that accepts 0n1n",is_0n1n,{"02","01"})

# _0_pow_n_1_pow_n_TM = TuringMachine(
#             states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'},
#             input_alphabet={'a', 'b'},
#             tape_symbols={'a', 'b', 'X', 'Y', 'B'},
#             transitions={
#                 ('q0', 'a'): Next('q1', 'B', 'R'),  
#                 ('q0', 'b'): Next('q2', 'B', 'R'),
#                 ('q0', 'B'): Next('q8', 'B', 'S'),
#                 ('q1', 'a'): Next('q3', 'a', 'R'),
#                 ('q1', 'b'): Next('q3', 'b', 'R'),
#                 ('q1', 'B'): Next('q8', 'B', 'S'),
#                 ('q2', 'a'): Next('q4', 'a', 'R'),
#                 ('q2', 'b'): Next('q4', 'b', 'R'),
#                 ('q2', 'B'): Next('q8', 'B', 'S'),
#                 ('q3', 'a'): Next('q3', 'a', 'R'),
#                 ('q3', 'b'): Next('q3', 'b', 'R'),
#                 ('q3', 'B'): Next('q5', 'B', 'L'),
#                 ('q4', 'a'): Next('q4', 'a', 'R'),
#                 ('q4', 'b'): Next('q4', 'b', 'R'),
#                 ('q4', 'B'): Next('q6', 'B', 'L'),
#                 ('q5', 'b'): Next('q7', 'B', 'L'),
                
#                 ('q6', 'b'): Next('q7', 'B', 'L'),
#                 ('q7', 'a'): Next('q7', 'a', 'L'),
#                 ('q7', 'b'): Next('q7', 'b', 'L'),
#                 ('q7', 'B'): Next('q0', 'B', 'R')

#             },
#             initial_state='q0',
#             accept_states={'q8'},
#             reject_states={'q9'}
#         )

# ## after you build it you need to add it to the controller and give it the same name  that was given by the TA:
# controller.add_turing_machine('0n1n', _0_pow_n_1_pow_n_TM)

# controller.visualize('0n1n','aaabbb',3)
# # #controller.submit()






# # language 0^n_1^n_2_0^n_1^n (2_0^n_1^n_2_0^n_1^n)*
# step1 = TuringMachine(
#             states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
#             input_alphabet={'0', '1', '2', 'X', 'Y', 'B','Z'},
#             tape_symbols={'0', '1', '2', 'X', 'Y', 'B','Z'},
#             transitions={
#                 ('q0', '0'): Next('q1', 'X', 'R'),  # Step 1 change 0 to X
#                 ('q0', 'Y'): Next('q3', 'Y', 'R'),
#                 ('q1', '0'): Next('q1', '0', 'R'),
#                 ('q1', '1'): Next('q2', 'Y', 'L'),
#                 ('q1', 'Y'): Next('q1', 'Y', 'R'),
#                 ('q2', '0'): Next('q2', '0', 'L'),
#                 ('q2', 'X'): Next('q0', 'X', 'R'),
#                 ('q2', 'Y'): Next('q2', 'Y', 'L'),
#                 ('q3', 'Y'): Next('q3', 'Y', 'R'),
#                 ('q3', 'B'): Next('q4', 'B', 'S'),

#                 ('q3', '2'): Next('q4', '2', 'S')
#             },
#             initial_state='q0',
#             accept_states={'q4'},
#             reject_states={'q5'}
#         )
# cond = TuringMachine( #current head pos equals 0
#             states={'q0', 'q1', 'q2', 'q3'},
#             input_alphabet={'0', '1','2' , 'X', 'Y', 'B','Z'},
#             tape_symbols={'0', '1','2', 'X', 'Y', 'B','Z'},
#             transitions={
#                 ('q0', 'X'): Next('q0', 'X', 'R'),
#                 ('q0', 'Y'): Next('q0', 'Y', 'R'),
#                 ('q0', '2'): Next('q2', 'Z', 'R'),
#                 ('q0', 'Z'): Next('q0', 'Z', 'R')
#             },
#             initial_state='q0',
#             accept_states={'q2'},
#             reject_states={'q3'}
#         )
# dowhile = WhileTuringMachine("My Cond", cond, "My Do While", step1)
# # combined_tm.add('find_a_n_b_n', step1)
# #combined_tm.add('Move Left to Leftmost 0', step4)

# #you want to repeat steps number 01 until no more 2 remain in the tape
# # combined_tm.setTuringMachineWhileCondition("2 still in tape", cond)
# ####################important step!!!! dont forget!!!##########################
# controller.add_turing_machine('doWhile',dowhile)


# controller.run_turing_machine('doWhile', "001120011")



# multi tape tm example

# # Example usage: Copy a binary string from tape 1 to tape 2

# states = {'q0', 'q1', 'q2', 'qa', 'qr'}
# input_alphabet = {'0', '1'}
# tape_alphabet = {'0', '1', 'B'}
# transition_function = {
#     # (current_state, tape1_symbol, tape2_symbol): (new_state, tape1_new_symbol, tape2_new_symbol, direction1, direction2)
#     ('q0', '0', 'B'): MultiNext('q1', '0', '0', 'R', 'R'),
#     ('q0', '1', 'B'): MultiNext('q1', '1', '1', 'R', 'R'),
#     ('q0', 'B', 'B'): MultiNext('qa', 'B', 'B', 'S', 'S'),

#     ('q1', '0', 'B'): MultiNext('q1', '0', '0', 'R', 'R'),
#     ('q1', '1', 'B'): MultiNext('q1', '1', '1', 'R', 'R'),
#     ('q1', 'B', 'B'): MultiNext('qa', 'B', 'B', 'S', 'S'),
# }
# start_state = 'q0'
# accept_state = {'qa'}
# reject_state = {'qr'}




# tm1 = MultiTapeTuringMachine(
#     states={'q0', 'q1', 'q2', 'qa', 'qr'},
#     input_alphabet={'0', '1', 'X'},
#     tape_alphabet={'0', '1', 'B', 'X'},
#     transition_function= {
#     # (current_state, tape1_symbol, tape2_symbol): (new_state, tape1_new_symbol, tape2_new_symbol, direction1, direction2)
#     ('q0', '0'): MultiNext('q1', '0', 'L'),
#     ('q0', '1'): MultiNext('q1',  '1', 'L'),
#     ('q0', 'B'): MultiNext('q1',  'B', 'L'),
#     ('q1', '0'): MultiNext('q1', '0', 'L'),
#     ('q1', '1'): MultiNext('q1',  '1', 'L'),
#     ('q1', 'X'): MultiNext('qa',  'X', 'R')
# },
#     start_state='q0',
#     accept_state={'qa'},
#     reject_state={'qr'},
#     num_tapes=1
# )

# tm2 = MultiTapeTuringMachine(
#     states={'q0', 'q1', 'q2', 'qa', 'qr'},
#     input_alphabet={'0', '1', 'X'},
#     tape_alphabet={'0', '1', 'B', 'X'},
#     transition_function= {
#     # (current_state, tape1_symbol, tape2_symbol): (new_state, tape1_new_symbol, tape2_new_symbol, direction1, direction2)
#     ('q0', '0'): MultiNext('q0', '1', 'R'),
#     ('q0', '1'): MultiNext('q0',  '0', 'R'),
#     ('q0', 'B'): MultiNext('qa',  'B', 'S')
# },
#     start_state='q0',
#     accept_state={'qa'},
#     reject_state={'qr'},
#     num_tapes=1
# )

# tm3 = MultiTapeTuringMachine(
#     states={'qs', 'q0', 'q1', 'q2', 'q3', 'qa', 'qr'},
#     input_alphabet={'0', '1'},
#     tape_alphabet={'0', '1', 'B', 'X'},
#     transition_function= {
#     # (current_state, tape1_symbol, tape2_symbol): (new_state, tape1_new_symbol, tape2_new_symbol, direction1, direction2)
#     ('qs', '0', 'B'): MultiNext('q0', '0', 'X', 'S', 'R'),
#     ('qs', '1', 'B'): MultiNext('q0', '1', 'X', 'S', 'R'),
#     ('qs', 'B', 'B'): MultiNext('qa', 'B', 'B', 'S', 'S'),

#     ('q0', '0', 'B'): MultiNext('q1', '0', '0', 'R', 'R'),
#     ('q0', '1', 'B'): MultiNext('q1', '1', '1', 'R', 'R'),
#     ('q0', 'B', 'B'): MultiNext('qa', 'B', 'B', 'S', 'S'),

#     ('q1', '0', 'B'): MultiNext('q1', '0', '0', 'R', 'R'),
#     ('q1', '1', 'B'): MultiNext('q1', '1', '1', 'R', 'R'),
#     ('q1', 'B', 'B'): MultiNext('q2', 'B', 'B', 'S', 'S'),
#     ('q2', 'B', 'B') : Call_Turing_Machine("move left on tape 2", tm1, [1], 'q3', 'qr'),

#     ('q3', 'B', '0') : Call_Turing_Machine("replace 0 and 1", tm2, [1], 'qa', 'qr'),
#     ('q3', 'B', '1') : Call_Turing_Machine("replace 0 and 1", tm2, [1], 'qa', 'qr')
# },
#     start_state='qs',
#     accept_state={'qa'},
#     reject_state={'qr'},
#     num_tapes=2
# )

# controller.update_turing_machine("multi", tm3)


# inputs = ['1101', '']
# #result = tm.run(inputs)
# controller.run_turing_machine("multi", inputs)
#controller.run_turing_machine("multi", inputs)
#tm2.visualize(['1101', ''],1)
#controller.visualize_step_by_step("multi", inputs)

#print(tm3)

# def binReplaceFunc(bin_str):
#     res = ""
#     if(bin_str == ""):
#         return ""
#     for x in bin_str:
#         if x == "1":
#             res += '0'
#         elif x == "0":
#             res += '1'
#     return res


# controller.add_challenge('addbin', {'0','1'}, "bin add", binReplaceFunc, {"111"})



# tm3 = MultiTapeTuringMachine(
#     states={'q0', 'q1', 'qa', 'qr'},
#     input_alphabet={'0', '1'},
#     tape_alphabet={'0', '1', 'B'},
#     transition_function= {
#     # (current_state, tape1_symbol, tape2_symbol): (new_state, tape1_new_symbol, tape2_new_symbol, direction1, direction2)
#     ('q0', '0'): MultiNext('q0', '1', 'R'),
#     ('q0', '1'): MultiNext('q0',  '0', 'R'),
#     ('q0', 'B'): MultiNext('qa',  'B', 'L')
# },
#     start_state='q0',
#     accept_state={'qa'},
#     reject_state={'qr'},
#     num_tapes=1
# )


# # # turing machine increments number 1

# # controller.add_turing_machine("addbin", tm3, "tape")

# # #controller.run_turing_machine("addbin", ["1"])

# controller.visualize("addbin", ["1"])

# # controller.validate_turing_machineTA("addbin")



#####################################################################################
# # concatenate tms example
# simple_turing_machine_1 = TuringMachine(  # this machine converts first encountered 0 to 1
#             states={'q0', 'q1', 'q2'},
#             input_alphabet={'0', '1','2'},
#             tape_symbols={'0', '1', 'B','2'},
#             transitions={
#                 ('q0', '0'): Next('q1', '1', 'R'),  # if encountered 0 put 1 and move right
#                 ('q0', '1'): Next('q0', '1', 'R'),  # if encountered 1 just move right
#                 ('q0', 'B'): Next('q1', 'B', 'S'),  # if encountered 1 just move right
#                 ('q1', '0'): Next('q1', '0', 'S'),  # after reaching q1 don't do anything
#                 ('q1', '1'): Next('q1', '1', 'S'),  # after reaching q1 don't do anything
#                 ('q1', 'B'): Next('q1', 'B', 'S'),  # after reaching q1 don't do anything
#             },
#             initial_state='q0',
#             accept_states={'q1'},
#             reject_states={'q2'}
#         )
# simple_turing_machine_2 = TuringMachine(# this machine converts first encountered 1 to 0
#             states={'q0', 'q1', 'q2'},
#             input_alphabet={'0', '1'},
#             tape_symbols={'0', '1', 'B'},
#             transitions={
#                 ('q0', '0'): Next('q0', '0', 'R'),  # if encountered 0 just move right
#                 ('q0', '1'): Next('q1', '0', 'R'),  # if encountered 1 put 0 and move right
#                 ('q0', 'B'): Next('q1', 'B', 'S'),
#                 ('q1', '0'): Next('q1', '0', 'S'),  # after reaching q1 don't do anything
#                 ('q1', '1'): Next('q1', '1', 'S'),  # after reaching q1 don't do anything
#                 ('q1', 'B'): Next('q1', 'B', 'S'),  # after reaching q1 don't do anything

#             },
#             initial_state='q0',
#             accept_states={'q1'},
#             reject_states={'q2'}
#         )

# combined_tm = ConcatenateTM("step1", simple_turing_machine_1, "step2", simple_turing_machine_2)


# ####################important step!!!! dont forget!!!##########################
# controller.add_turing_machine('Contan',combined_tm)

# controller.run_turing_machine('Contan', "000111")









#####################################################################

# _0_pow_n_1_pow_n_TM = TuringMachine(
#             states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
#             input_alphabet={'0', '1'},
#             tape_symbols={'0', '1', 'X', 'Y', 'B'},
#             transitions={
#                 ('q0', '0'): Next('q1', 'X', 'R'),  # Step 1 change 0 to X
#                 ('q0', 'Y'): Next('q3', 'Y', 'R'),
#                 ('q1', '0'): Next('q1', '0', 'R'),
#                 ('q1', '1'): Next('q2', 'Y', 'L'),
#                 ('q1', 'Y'): Next('q1', 'Y', 'R'),
#                 ('q2', '0'): Next('q2', '0', 'L'),
#                 ('q2', 'X'): Next('q0', 'X', 'R'),
#                 ('q2', 'Y'): Next('q2', 'Y', 'L'),
#                 ('q3', 'Y'): Next('q3', 'Y', 'R'),
#                 ('q3', 'B'): Next('q4', 'B', 'L')
#             },
#             initial_state='q0',
#             accept_states={'q4'},
#             reject_states={'q5'}
#         )

# ## after you build it you need to add it to the controller and give it the same name  that was given by the TA:
# controller.add_turing_machine('0n1n', _0_pow_n_1_pow_n_TM, "bool")


# #controller.visualize_step_by_step('0n1n',"01")

# controller.validate_turing_machine('0n1n',is_0n1n)








# cond = TuringMachine( # 1 occurences in tape is more than 2
#             states={'q0', 'q1', 'qa', 'qr'},
#             input_alphabet={'0', '1'},
#             tape_symbols={'0', '1', 'B'},
#             transitions={
#                 ('q0', '0'): Next('q0', '0', 'R'),
#                 ('q0', '1'): Next('q1', '1', 'R'),
#                 ('q0', 'B'): Next('qr', 'B', 'S'),
#                 ('q1', '0'): Next('q0', '0', 'R'),
#                 ('q1', '1'): Next('qa', '1', 'R'),
#                 ('q1', 'B'): Next('qr', 'B', 'S'),
#             },
#             initial_state='q0',
#             accept_states={'qa'},
#             reject_states={'qr'}
#         )
# do = TuringMachine( # replace the first 1 to 0
#             states={'q0', 'q1', 'qa', 'qr'},
#             input_alphabet={'0', '1'},
#             tape_symbols={'0', '1', 'B'},
#             transitions={
#                 ('q0', '0'): Next('q0', '0', 'R'),
#                 ('q0', '1'): Next('qa', '0', 'R'),
#                 ('q0', 'B'): Next('qr', 'B', 'S') 
#             },
#             initial_state='q0',
#             accept_states={'qa'},
#             reject_states={'qr'}
#         )

# whileTM = WhileTuringMachine("1 occurences in tape is more than 2", cond, "replace 1 to 0", do)
# controller.add_turing_machine("whileTM", whileTM)

# controller.run_turing_machine('whileTM', "1011001")
