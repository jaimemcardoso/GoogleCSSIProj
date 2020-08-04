import webapp2
import jinja2
import os
import random
import logging
from google.appengine.api import users

the_jinja_env = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape=True)

animal_questions = {
"level1":"What is the fastest animal in the world? br Cheetah br peregrine_falcon br Swordfish br Vulture br 10",
"level2":"How long was the longest snake in captivity? br 25ft2in br 26ft br 22ft7in br 31ft3in ",
"level3":"Mysterious deaths of which creatures threaten agriculture? br Ants br Pandas br Bees br Rats ",
"level4":"Which animals swims in the upright position? br Dolphin br Flounder br Anglerfish br Seahorse",
"level5":"What animal is considered a farmers best friend? br Dog br Worm br Cat br Horse ",
"level6":"On average how many human years is equivalent to one dog year? br 15 br 7 br 13 br 22",
"level7":"What is the attention span of a goldfish? br 0.2seconds br 4seconds br 9seconds br 12seconds ",
"level8":"What is considered to be the most intelligent animal? br Chimpanzees br Orangutans br Gorillas br Dogs",
"level9":"What is considered to be the dumbest animal? br Cats br Domesticated_Turkey br Goldfish br Snakes ",
"level10":"What animal lives the longest? br Sharks br Parrots br Bowhead_Whales br Leopards ",
}



animal_correct_answers = {
"peregrine_falcon":"peregrine_falcon",
"25ft2in":"25ft2in",
"Bees":"Bees",
"Seahorse":"Seahorse",
"Worm":"Worm",
"15":"15",
"9seconds":"9seconds",
"Chimpanzees":"Chimpanzees",
"Domesticated_Turkey":"Domesticated_Turkey",
"Bowhead_Whales":"Bowhead_Whales",
}

coding_questions = {
"level1":"What is used to take input from the user in Python? br cin br scanf() br input() br <>",
"level2":"What is a function within a class called? br Definition br method br instance br object",
"level3":"Given the array colors=[red,blue,yellow,orange,magenta,teal] what color is in the position colors[4]? br Orange br magenta br Teal br Blue",
"level4":"What is the result of 5+5? br  55 br 10 br 5,5 br 5+5",
"level5":"What command shows the result in the browser? br console.log br console.write br document.log br document.write",
"level6":"What does the syntax != mean? br equal br not_equal br less_than br more_than",
"level7":"What is used to define a block of code (body of loop, function etc.) in Python? br curly_braces br Parenthesis br Indentation br Quotation",
"level8":"Who created python? br Guido_van_Rossum br Guido_van_Py br Gillian_Mo_Py br Gillian_Mo_Rossum",
"level9":"How to comment out in HTML? br ** br # br // br --",
"level10":"What is the name of the Python data type that is used to store keys and values, as opposed to indexes? br string br object br dictionary br operator",
}

coding_correct_answers = {
"input()":"input()",
"method":"method",
"magenta":"magenta",
"10":"10",
"document.write":"document.write",
"not_equal":"not_equal",
"Indentation":"Indentation",
"Guido_van_Rossum":"Guido_van_Rossum",
"//":"//",
"dictionary": "dictionary"
}

slogan_questions = {
"level1":"What companys slogan is Eat Fresh? br Wendys br Chick-fil-a br Acapulco br Subway",
"level2":"What companys slogan is Taste the Rainbow? br Hersheys br Skittles br Lindor br Dasani",
"level3":"What companys slogan is Snap! Crackle! Pop! br Rice_Krispies br Crunch br Popsockets br Google",
"level4":"What companys slogan is Because Youre Worth It? br Pantene br Old_Spice br Dove br Loreal",
"level5":"What companys slogan is Grace Space Pace? br Maserati br Porsche br Jaguar br Ferrari",
"level6":"What companys slogan is Theyre GR-R-R-reat! br Fruit_Loops br Kelloggs_Frosties br Coco_Puffs br Lucky_Charms",
"level7":"What companys slogan is Whats The Worst That Could Happen? br Coca-Cola br Root_Beer br Sprite br Dr.Pepper",
"level8":"What companys slogan is It Gives You Wiiiings! br Wingstop br Red_Bull br Wings_n_More br Monster",
"level9":"What companys slogan is Every Little Helps? br Tesco br H.E.B. br Walmart br Safeway",
"level10":"What companys slogan is Vorsprung durch Technik? br Volkswagon br Bayer_Corporation br Audi br Munich_Reinsurance_America",
}

slogan_correct_answers = {
"Subway":"Subway",
"Skittles":"Skittles",
"Rice_Krispies":"Rice_Krispies",
"Loreal":"Loreal",
"Jaguar":"Jaguar",
"Kelloggs_Frosties":"Kelloggs_Frosties",
"Dr.Pepper":"Dr.Pepper",
"Red_Bull":"Red_Bull",
"Tesco":"Tesco",
"Audi":"Audi",
}


player = ""
score=0

class generalClass(webapp2.RequestHandler): #starting page
    def get(self):
        global player
        player=str(self.request.get('name'))
        template = the_jinja_env.get_template('quiz.html')
        a_dictionary = {
            "greeting":"Ex-Quiz-It </>",
            'mode': 1,
            'player':player,
        }
        self.response.out.write(template.render(a_dictionary))

class chooseGeneral(webapp2.RequestHandler): #category chooser
    def post(self):
        global player
        global score
        player=str(self.request.get('name'))
        template = the_jinja_env.get_template('quiz.html')
        b_dictionary = {
            "greeting":"Ex-Quiz-It </>",
            'mode': 2,
            'stage': "Categories ",
            'player':player,
            'score':score,
        }
        self.response.write(template.render(b_dictionary))

class animalsGeneral(webapp2.RequestHandler): #chose your question based on points
    def get(self):
        template = the_jinja_env.get_template('quiz.html')
        animals_dictionary = {
            "greeting":"Ex-Quiz-It </>",
            'mode': 3,
            'level': "Choose your Question",
            'player': player,
        }
        self.response.write(template.render(animals_dictionary))

class animalQuestions(webapp2.RequestHandler): #chose your question based on points
    def get(self):
        template = the_jinja_env.get_template('quiz.html')
        level_var = self.request.get("id")
        values = animal_questions[level_var].split("br")

        if (level_var in animal_questions):
            question = animal_questions[level_var]

        question = {
            "greeting":"Ex-Quiz-It </>",
            "mode":4,
            "animal_questions" :animal_questions,
            "level": level_var,
            "question":values[0],
            'ans1':values[1],
            'ans2':values[2],
            'ans3':values[3],
            'ans4':values[4],
            'score':score,
            'player': player,
        }
        self.response.write(template.render(question))

    def post(self):
        template = the_jinja_env.get_template('quiz.html')
        global score
        global player
        correct_ans = ""
        incorrect_ans = ""
        ansid = self.request.get("ans")
        if (ansid in animal_correct_answers):
            answer='That is correct!'
            score+=+10

        else:
            answer = "Incorrect"
            score=score-10

        answer = {
        "greeting":"Ex-Quiz-It </>",
        'player': player,
        'mode':9,
        'selected_answer' :answer,
        'score':score,
        }
        self.response.write(template.render(answer))


class codeGeneral(webapp2.RequestHandler): #chose your question based on points
    def get(self):
        global player
        template = the_jinja_env.get_template('quiz.html')
        code_dictionary = {
            "greeting":"Ex-Quiz-It </>",
            'mode': 5,
            'level': "Choose your level",
            'player':player,
        }
        self.response.write(template.render(code_dictionary))

class codingQuestions(webapp2.RequestHandler): #chose your question based on points
    def get(self):
        template = the_jinja_env.get_template('quiz.html')
        level_var = self.request.get("id")
        ansid = self.request.get("ans")
        values = coding_questions[level_var].split("br")

        if (level_var in coding_questions):
            question = (coding_questions[level_var])

        code = {
            'score': score,
            "greeting":"Ex-Quiz-It </>",
            "mode":6,
            "coding_questions" :coding_questions,
            "level": level_var,
            "question":values[0],
            'ans1':values[1],
            'ans2':values[2],
            'ans3':values[3],
            'ans4':values[4],
            'player': player,

        }
        self.response.write(template.render(code))
    def post(self):
        template = the_jinja_env.get_template('quiz.html')
        global score
        correct_ans = ""
        incorrect_ans = ""
        ansid = self.request.get("ans")
        if (ansid in coding_correct_answers):
            answer='That is correct!'
            score=score+10

        else:
            answer = "Incorrect"
            score=score-10

        code_answer = {
        "greeting":"Ex-Quiz-It </>",
        'mode':9,
        'selected_answer' :answer,
        'score':score,

        }
        self.response.write(template.render(code_answer))
class slogansGeneral(webapp2.RequestHandler):#chose your question based on points
    def get(self):
        template = the_jinja_env.get_template('quiz.html')
        slogans_dictionary = {
            "greeting":"Ex-Quiz-It </>",
            'mode': 7,
            'level': "Choose your level",
            'player':player,
        }
        self.response.write(template.render(slogans_dictionary))



class sloganQuestions(webapp2.RequestHandler): #chose your question based on points
    def get(self):
        template = the_jinja_env.get_template('quiz.html')
        level_var = self.request.get("id")
        ansid = self.request.get("ans")
        values = slogan_questions[level_var].split("br")

        if (level_var in slogan_questions):
            question = (slogan_questions[level_var])

        slogan = {
            'score': score,
            "greeting":"Ex-Quiz-It </>",
            "mode":8,
            "slogan_questions" :slogan_questions,
            "level": level_var,
            "question":values[0],
            'ans1':values[1],
            'ans2':values[2],
            'ans3':values[3],
            'ans4':values[4],
            'player': player,

        }
        self.response.write(template.render(slogan))
    def post(self):
        template = the_jinja_env.get_template('quiz.html')
        global score
        correct_ans = ""
        incorrect_ans = ""
        ansid = self.request.get("ans")
        if (ansid in slogan_correct_answers):
            answer='That is correct!'
            score=score+10

        else:
            answer = "Incorrect"
            score=score-10

        answer = {
        "greeting":"Ex-Quiz-It </>",
        'mode':9,
        'selected_answer' :answer,
        'score':score,

        }
        self.response.write(template.render(answer))

class Done(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('quiz.html')
        global score
        global player
        done = {
        "greeting":"Ex-Quiz-It </>",
        'mode': 10,
        'score': score,
        'player': player,
        }
        self.response.write(template.render(done))


application = webapp2.WSGIApplication([('/',generalClass),
                                    ('/choose',chooseGeneral),
                                    ('/animals',animalsGeneral),
                                    ('/animalQuestions',animalQuestions),
                                    ('/codingQuestions',codingQuestions),
                                    ('/sloganQuestions',sloganQuestions),
                                    ('/code',codeGeneral),
                                    ('/slogans',slogansGeneral),
                                    ('/done',Done)],
                                    debug=True)
