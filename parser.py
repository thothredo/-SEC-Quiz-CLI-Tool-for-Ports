#### This is a python code that I will use to test myself out with to get better scores on the SEC+ test ####
import os
import re

def parse_file(filespath):
    questions = []
    with open (filespath, "r") as f:
        lines = f.readlines()

        current_question = None
        
        for line in lines:
            stripped =line.strip()

            if stripped == "" or stripped.startswith("CompTIA") or stripped == "Your answer to this question is incorrect or incomplete.":
                if stripped == "Your answer to this question is incorrect or incomplete.":
                    if current_question:
                        questions.append(current_question)
                        current_question = None
                continue 
            elif line.startswith("   "):
                current_question["options"].append(stripped)
                if stripped.endswith("( Missed)"):
                    current_question["correct"].append(stripped)
            elif line.startswith(" "):
                current_question = {"question": stripped, "options": [], "correct": []}
    return questions 

def parse_all_files(folder_path):
    all_questions = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            full_path = os.path.join(folder_path, filename)
            all_questions.extend(parse_file(full_path))
    return all_questions
