from flask import Flask, render_template, request, session
from parser import parse_all_files
import random

app = Flask(__name__)
app.secret_key = 'secplus'

questions = parse_all_files('/home/thoth/Claude/SEC+/CompTIA Security+ Certification Exam SY0-701 Practice Tests/')

@app.route('/')
def index():
    session['score'] = 0
    session['total'] = 0
    selected = random.sample(questions, 25)
    session['questions'] = selected
    session['current'] = 0
    return render_template('question.html',
                           question=selected[0],
                           number=1, 
                           total=25)

@app.route('/answer', methods=['POST'])
def answer():
    user_answer = request.form.get('answer')                                                                                                                              
    current = session['current']                                                                                                                                          
    questions_list = session['questions']
    question = questions_list[current]                                                                                                                                    
   
    options_clean = [opt.replace(' ( Missed)', '') for opt in question['options']]                                                                                        
    correct_answers = [opt.replace(' ( Missed)', '') for opt in question['correct']]
                                                                                                                                                                            
    try:        
        selected = [options_clean[int(i) - 1] for i in user_answer.split(',')]                                                                                            
        if set(selected) == set(correct_answers):                                                                                                                         
            result = 'correct'
            session['score'] += 1                                                                                                                                         
        else:   
            result = 'wrong'                                                                                                                                              
    except:     
        result = 'invalid'

    session['current'] += 1                                                                                                                                               
    session['total'] += 1
                                                                                                                                                                            
    return render_template('answer.html',
                            result=result,
                            correct_answers=correct_answers,
                            number=current + 1,                                                                                                                            
                            total=25)
@app.route('/next')                                                                                                                                                       
def next_question():                                                                                                                                                      
    current = session['current']                                                                                                                                          
    if current >= 25:                                                                                                                                                     
        return render_template('score.html', score=session['score'], total=25)
    question = session['questions'][current]                                                                                                                              
    return render_template('question.html',
                            question=question,                                                                                                                             
                            number=current + 1,                                                                                                                            
                            total=25)

if __name__=='__main__':
    app.run(debug=True)

