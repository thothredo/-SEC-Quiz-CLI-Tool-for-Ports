
from parser import parse_file                                                                                                                                             
                                                                                                                                                                            
q = parse_file('/home/thoth/Claude/SEC+/CompTIA Security+ Certification Exam SY0-701 Practice Tests/CompTIA Security+ Certification Exam SY0-701 Practice Test 1.txt')    
                                                                                                                                                                            
print('Total questions:', len(q))                                                                                                                                         
print('First question:', q[0])