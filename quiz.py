from parser import parse_all_files                                                                                                                                        
import random                                                                                                                                                             
                                                                                                                                                                            
questions = parse_all_files('/home/thoth/Claude/SEC+/CompTIA Security+ Certification Exam SY0-701 Practice Tests/')
                                                                                                                                                                            
score = 0       
total = 25
                                                                                                                                                                            
selected_questions = random.sample(questions, total)
                                                                                                                                                                            
for question in selected_questions:
    print(question["question"])
    for i, option in enumerate(question["options"], 1):
        print(f" {i}. {option.replace('( Missed)', '')}")
    answer = input("\nYour answer: ")                                                                                                                                     
    options_clean = [opt.replace(' ( Missed)', '') for opt in question["options"]]
    correct_answers = [opt.replace(' ( Missed)', '') for opt in question["correct"]]
    if not correct_answers:
        continue                                                                                    
    print("\nCorrect answer:")                                                                                                                                            
    for ans in correct_answers:
         print(f" - {ans}")                                                                                                                                                
    try:        
        selected = [options_clean[int(i) - 1] for i in answer.split(',')]
        if set(selected) == set(correct_answers):
            print("correct")                                                                                                                                              
            score += 1
        else:                                                                                                                                                             
            print("wrong")
    except:
        print("Invalid input")
print(f"\nYou scored {score}/{total}")