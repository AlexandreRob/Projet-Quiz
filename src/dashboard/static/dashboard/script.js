// quizz 31_1 
const quizData = [
    {
        question: "Un échafaudage mi-lourd est un :",
        a: "Echafaudage de pied de grande hauteur",
        b: "Echafaudage de peintre",
        c: "Echafaudage de soutien et d'étaiement",
        d: "Echafaudage sur tréteaux",
        correct: "d",
    },
    {
        question: "L'improvisation d'un échafaudage :",
        a: "Prouve l'autonomie du maçon",
        b: "Est un critère d'adaptation propre aux maçons",
        c: "Améliore les performances d'organisation du chantier",
        d: "Peut avoir des conséquences graves pour la sécurité des utilisateurs",
        correct: "d",
    },
    {
        question: "Un échafaudage sur tréteaux est constitué de :",
        a: "Pieds, portiques, plateaux, garde corps, échelles clavettes et diagonales",
        b: "De tréteaux réglables, pieds démontables ou fixes, d'un platelage et de garde corps amovibles",
        c: "De tréteaux réglables, pieds amovibles, d'un platelage, d'un garde corps, de portails d'abouts et de jambes de maintien",
        d: "Aucune de ces réponses",
        correct: "b",
    },
    {
        question: "Les tréteaux sont réglables en hauteur jusqu'à :",
        a: "1,50 m",
        b: "2,00 m",
        c: "2,50 m",
        d: "3,00 m",
        correct: "b",
    },
    {
        question: "Quelle est la hauteur maximum du plancher pour un échafaudage sur tréteaux muni de portiques complémentaires :",
        a: "2,60 m",
        b: "3,40 m",
        c: "3,60 m",
        d: "4,60 m",
        correct: "a",
    },
   



];

const quiz= document.getElementById('quiz')
const answerEls = document.querySelectorAll('.answer')
const questionEl = document.getElementById('question')
const a_text = document.getElementById('a_text')
const b_text = document.getElementById('b_text')
const c_text = document.getElementById('c_text')
const d_text = document.getElementById('d_text')
const submitBtn = document.getElementById('submit')


let currentQuiz = 0
let score = 0

loadQuiz()

function loadQuiz() {

    deselectAnswers()

    const currentQuizData = quizData[currentQuiz]

    questionEl.innerText = currentQuizData.question
    a_text.innerText = currentQuizData.a
    b_text.innerText = currentQuizData.b
    c_text.innerText = currentQuizData.c
    d_text.innerText = currentQuizData.d
}

function deselectAnswers() {
    answerEls.forEach(answerEl => answerEl.checked = false)
}

function getSelected() {
    let answer
    answerEls.forEach(answerEl => {
        if(answerEl.checked) {
            answer = answerEl.id
        }
    })
    return answer
}


submitBtn.addEventListener('click', () => {
    const answer = getSelected()
    if(answer) {
       if(answer === quizData[currentQuiz].correct) {
           score++
       }

       currentQuiz++

       if(currentQuiz < quizData.length) {
           loadQuiz()
       } else {
           quiz.innerHTML = `
           <h2>Votre score est de ${score}/${quizData.length} </h2>

           <button onclick="location.reload()">refaire le quizz</button>
           `
       }
    }
})