const questions = [
    {
        question: "What are you doing?",
        choices: [
            'Working',
            'Playing',
            'Chatting',
            'Something',
        ],
        correctAnswer: 'Working'
    },
    {
        question: "Hello",
        choices: [
            '1',
            '2',
            '3',
            '4',
        ],
        correctAnswer: 'Working'
    }
];

const questions_div = document.getElementById("questions");
const answers_div = document.getElementById("answers");


function firstAppend(randomIndex){
    // First Question Append
    const question = document.createElement("h2");
    question.innerText = questions[randomIndex]['question'];
    question.id = "quest";
    questions_div.appendChild(question);

    // First Answers Append
    for (let i = 0; i < 4; i++) {
        const input = document.createElement("input");
        const answer = document.createElement("label");
        
        input.type = 'radio';
        input.name = "rad";

        answer.innerText = questions[randomIndex]['choices'][i];
        answer.id = 'answer' + i;

        answers_div.appendChild(input);
        answers_div.appendChild(answer);
        answers_div.appendChild(document.createElement("br"));
    }
}


function showQuestion(index){
    const question = document.getElementById("quest");
    question.innerText = questions[index]['question'];
}


function showAnswers(index){
    const answers = [];

    for (let i = 0; i < 4; i++) {
        answers.push(document.getElementById('answer' + i));      
    }

    for (let i = 0; i < answers.length; i++) {
        answers[i].innerText = questions[index]['choices'][i];  
    }

}


function checkCorrectAnswer(index){
    
}

 
 
firstAppend(0);
showQuestion(1);
showAnswers(1);


