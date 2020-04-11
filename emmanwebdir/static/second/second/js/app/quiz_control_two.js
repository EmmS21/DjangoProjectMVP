var star = '<svg id="star" x="0px" y="0px" viewBox="0 0 512.001 512.001"><path fill="#ffdc64" d="M499.92 188.26l-165.84-15.38L268.2 19.9c-4.6-10.71-19.8-10.71-24.4 0l-65.88 152.97-165.84 15.38c-11.61 1.08-16.3 15.52-7.54 23.22L129.66 321.4 93.04 483.87c-2.56 11.38 9.73 20.3 19.75 14.35L256 413.2l143.2 85.03c10.03 5.96 22.32-2.97 19.76-14.35L382.34 321.4l125.12-109.92c8.77-7.7 4.07-22.14-7.54-23.22z"/><path fill="#ffc850" d="M268.2 19.91c-4.6-10.71-19.8-10.71-24.4 0l-65.88 152.97-165.84 15.38c-11.61 1.08-16.3 15.52-7.54 23.22L129.66 321.4 93.04 483.87c-2.56 11.38 9.73 20.3 19.75 14.35l31.97-18.98c4.42-182.1 89.03-310.33 156.02-383.7L268.2 19.92z"/></svg>';

//Initialisation of variables
var currentQuestion = -1;
var tokens = 200;

var questions =[
		{
		"id":"q0",
		"topic":"Probability: Intro",
		"weight":2,
		"questionTxt": "Assume we have a packet of pens. This packet contains; 4 blue pens, 2 red pens and 3 black pens. If we randomly pick a pen from the packet, replace the pen and repeat the process 2 additional times. What is the probability of drawing 2 blue pens and 1 black pen?",
		"hint": "We want the probability of drawing 2 black pens and 1 black pen",
		"options":[
			{
				"optionTxt": "26/243",
				"answer": false
			},
			{
				"optionTxt": "16/243",
				"answer": true
			},
			{
				"optionTxt": "32/243",
				"answer": false
			},
			{
				"optionTxt": "8/243",
				"answer": false
			}
		],
		"feedback":"Probability of drawing 2 blue pens and 1 black pen = 4/9 * 4/9 * 3/9 = 48/729 = 16/243."
	},
	{
		"id":"q1",
		"topic":"Probability: Intro",
		"weight":1,
		"questionTxt": "Let’s assume we flip a coin twice. What is the probability of the coin landing on heads two consecutive times?",
		"hint": "Remember that each coin toss is an independent event, meaning the outcome of the first does not impact the outcome of the second toss",
		"options":[
			{
				"optionTxt": "1/4",
				"answer": true
			},
			{
				"optionTxt": "1/2",
				"answer": false
			},
			{
				"optionTxt": "3/4",
				"answer": false
			},
			{
				"optionTxt": "2/3",
				"answer": false
			}
		],
		"feedback":"1/2 * 1/2 = 1/4"
	},
	{
		"id":"q2",
		"topic":"Probability: Intro",
		"weight":3,
		"questionTxt": "Calculate the probability of selecting a black card or a 6 from a deck of 52 cards?",
		"hint": "Remember that you are calculating the probability of P(Black or 6). Start of by calculating the probability of selecting a black card, then selecting a 6",
		"options":[
			{
				"optionTxt": "5/13",
				"answer": false
			},
			{
				"optionTxt": "9/13",
				"answer": false
			},
			{
				"optionTxt": "2/13",
				"answer": false
			},
			{
				"optionTxt": "7/13",
				"answer": true
			}
		],
		"feedback":"P(B) = 26/52 -> P(6) = 4/52 -> P(B) + P(6P - P(B and 6) -> 26/52 + 4/52 - 2/52 = 28/52 or 7/13"
	},
];

if(currentQuestion==-1){
	questionInit();
}
//--------------------------------------------------------------------------------------
    //Logic for the options
$('.option').click(function(){
    //only one option can be checked
	$('.option').removeClass('checked');
	$(this).toggleClass('checked');
	var questionSelected = $('#question-options .checked').length;
	if(questionSelected===1){
		$('#question .submit').css('display','flex');
	}
});
//end logic for options
	//--------------------------------------------------------------------------------------
    //logic for end of test + animations
$('#question .submit').click(function(){
	$('.hint, #hint').hide();
	$('#question .submit').css('display','none');
	 if(currentQuestion === questions.length-1){
			$('.nextQ').hide();
		}else{
			$('#question .nextQ').css('display','flex');
		}

	$('#question .feedback').css('display','flex');
	$('.option').addClass('disabled');
	$('.option').find('.textOpt').toggleClass('hide');

	//add for each options if this is or not the right answer - For only 4 options
// 	for(var i=0; i<4; i++){
// 		console.log($('#opt'+i).data("result"))

// 	}


});
//end of logic for end of test + animations

//logic for the feedback
$('.feedback').click(function(){
	$(this).addClass('disabled');
	var feedback = $('#feedback');
	var feedbackText = $('#feedback p');
	var feedbackTitle = $('#feedback h1');

$('#feedback').append('<h2>Feedback</h2><p>'+questions[currentQuestion].feedback+'</p>');
		TweenLite.to(feedback, 0.5, {opacity:"1"});
});

//Logic for the hint button
$('.hint').click(function(){
	// $(this).addClass('disabled');
	var hint = $('#hint');
	if(hint.hasClass('hide')){
	    hint.toggleClass('hide');
	}
	else if(hint.hasClass('hide')==false){
		hint.toggleClass('hide');
	}
});

//Logic for the next button
$('.nextQ').click(function(){
		$('.feedback, .hint').removeClass('disabled');
		$('.hint, #hint').hide();
		$('.option').find('svg').remove();
		questionInit();
});

function questionInit(){
	 //reinitialise for each questions the variables and the style + some info in the console
	$('.option').removeClass('checked');
	$('#question .btn').css('display','none');
	$('#feedback').empty();
	$('#hint').empty();
	$('#hint').addClass('hide');
	$('.feedback, .hint, .option').removeClass('disabled');
	$('.hint, #hint').show();

	max=0;
  currentQuestion++;

  console.warn("--------------------------------------------------------")
  console.warn("Question "+ (currentQuestion + 1));
  console.warn(questions[currentQuestion].questionTxt);
  console.warn("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")
	//--------------------------------------------------------------------------------------
    //append the question from the array question
	$('#question-text h1').html("Question "+ (currentQuestion + 1) + " - "+questions[currentQuestion].topic);
	$('#question-text p').html(questions[currentQuestion].questionTxt);
	$('#hint').append('<h2>Hint</h2><p>'+questions[currentQuestion].hint+'</p>');

	for(var i=0; i<4; i++){
		var opt = '#opt'+i;
		var label = i+1;
		var text = questions[currentQuestion].options[i].optionTxt;
		var data = questions[currentQuestion].options[i].answer;

		$(opt).html('<div class="label" data-label="'+label+'"></div>'+'<div class="textOpt">'+text+'</div>');

		$(opt).data('r', data);
		if($(opt).data("r") === true){
			$(opt).find('.textOpt').addClass('right hide');
		}else{
			$(opt).find('.textOpt').addClass('wrong hide');
		}
	}

}
