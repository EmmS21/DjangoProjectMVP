var star = '<svg id="star" x="0px" y="0px" viewBox="0 0 512.001 512.001"><path fill="#ffdc64" d="M499.92 188.26l-165.84-15.38L268.2 19.9c-4.6-10.71-19.8-10.71-24.4 0l-65.88 152.97-165.84 15.38c-11.61 1.08-16.3 15.52-7.54 23.22L129.66 321.4 93.04 483.87c-2.56 11.38 9.73 20.3 19.75 14.35L256 413.2l143.2 85.03c10.03 5.96 22.32-2.97 19.76-14.35L382.34 321.4l125.12-109.92c8.77-7.7 4.07-22.14-7.54-23.22z"/><path fill="#ffc850" d="M268.2 19.91c-4.6-10.71-19.8-10.71-24.4 0l-65.88 152.97-165.84 15.38c-11.61 1.08-16.3 15.52-7.54 23.22L129.66 321.4 93.04 483.87c-2.56 11.38 9.73 20.3 19.75 14.35l31.97-18.98c4.42-182.1 89.03-310.33 156.02-383.7L268.2 19.92z"/></svg>';

//Initialisation of variables
var currentQuestion = -1;
var tokens = 200;

var questions =[
		{
		"id":"q0",
		"topic":"Bayesian Theory",
		"weight":2,
		"questionTxt": "Epidemiologists claim that the probability of breast cancer among Caucasian women in their mid-50s is 0.005. An established test identified people who had breast cancer and those that were healthy. A new mammography test in clinical trials has a probability of 0.85 for detecting cancer correctly. In women without breast cancer, it has a chance of 0.925 for a negative result. If a 55-year-old Caucasian woman tests positive for breast cancer, what is the probability that she, in fact, has breast cancer?",
		"hint": "Remember the formula: P(A|B) = ( P(A)P(B|A) )/ P(B)",
		"options":[
			{
				"optionTxt": "0.00425",
				"answer": false
			},
			{
				"optionTxt": "0.054",
				"answer": true
			},
			{
				"optionTxt": "0.00033521875",
				"answer": false
			},
			{
				"optionTxt": "0.91891",
				"answer": false
			}
		],
		"feedback":"(0.005 * 0.85)/ (0.005 * 0.85 + 0.995 * 0.075) = 0.054"
	},
	{
		"id":"q1",
		"topic":"Bayesian Theory",
		"weight":1,
		"questionTxt": "A diagnostic test has a probability0.95 of giving a positive result when applied to a person suffering from a certain disease, and a probability0.10 of giving a (false) positive when applied to a non-sufferer. It is estimated that 0.5 % of the population are sufferers. Suppose that the test is now administered to a person about whom we have no relevant information relating to the disease (apart from the fact that he/she comes from this population). Calculate the following probabilities that, given a negative result, the person is a non-sufferer.",
		"hint": "Remember that each coin toss is an independent event, meaning the outcome of the first does not impact the outcome of the second toss",
		"options":[
			{
				"optionTxt": "0.9997",
				"answer": true
			},
			{
				"optionTxt": "0.802",
				"answer": false
			},
			{
				"optionTxt": "0.891",
				"answer": false
			},
			{
				"optionTxt": "0.806",
				"answer": false
			}
		],
		"feedback":"(0.9 × 0.995)/ (1 − 0.10425) = 0.9997"
	},
	{
		"id":"q2",
		"topic":"Bayesian Theory",
		"weight":3,
		"questionTxt": "A diagnostic test has a probability0.95 of giving a positive result when applied to a person suffering from a certain disease, and a probability0.10 of giving a (false) positive when applied to a non-sufferer. It is estimated that 0.5 % of the population are sufferers. Suppose that the test is now administered to a person about whom we have no relevant information relating to the disease (apart from the fact that he/she comes from this population). Calculate the following probabilities that, given a positive result, the person is a sufferer",
		"hint": "Remember that you are calculating the probability of P(Black or 6). Start of by calculating the probability of selecting a black card, then selecting a 6",
		"options":[
			{
				"optionTxt": " 0.9997",
				"answer": false
			},
			{
				"optionTxt": "0.0995",
				"answer": false
			},
			{
				"optionTxt": "0.891",
				"answer": false
			},
			{
				"optionTxt": "0.0455",
				"answer": true
			}
		],
		"feedback":"(0.95 × 0.005) / ( (0.95 × 0.005) + (0.1 × 0.995) ) = 0.0455"
	},
	{
		"id":"q3",
		"topic":"Bayesian Theory",
		"weight":3,
		"questionTxt": "In a casino in Blackpool there are two slot machines: one that pays out 10 % of the time, and one that pays out 20 % of the time. Obviously, you would like to play on the machine that pays out 20 % of the time but you do not know which of the two machines is the more generous. You thus adopt the following strategy: you assume initially that the two machines are equally likely to be the generous machine. You then select one of the two machines at random and put a coin into it. Given that you lose that first bet estimate the probability that the machine you selected is the more generous of the two machines.",
		"hint": "Remember that you are calculating the probability of P(Black or 6). Start of by calculating the probability of selecting a black card, then selecting a 6",
		"options":[
			{
				"optionTxt": " 0.350",
				"answer": false
			},
			{
				"optionTxt": "0.08",
				"answer": false
			},
			{
				"optionTxt": "0.50",
				"answer": false
			},
			{
				"optionTxt": "0.471",
				"answer": true
			}
		],
		"feedback":"The probability that you are on the more generous machine given you lose the first game is 0.471"
	},
	{
		"id":"q4",
		"topic":"Bayesian Theory",
		"weight":3,
		"questionTxt": "1% of the population has X disease. A screening test accurately detects the disease for 90% if people with it. The test also indicates the disease for 15% of the people without it (the false positives). Suppose a person screened for the disease tests positive. What is the probability they have it?",
		"hint": "Remember that you are calculating the probability of P(Black or 6). Start of by calculating the probability of selecting a black card, then selecting a 6",
		"options":[
			{
				"optionTxt": " 0.00758",
				"answer": false
			},
			{
				"optionTxt": "0.1665",
				"answer": false
			},
			{
				"optionTxt": "0.00142",
				"answer": false
			},
			{
				"optionTxt": "0.0571",
				"answer": true
			}
		],
		"feedback":"P(D|T)= 0.009/0.1575 = 0.0571"
	},
	{
		"id":"q5",
		"topic":"Bayesian Theory",
		"weight":3,
		"questionTxt": "A diagnostic test has a probability 0.95 of giving a positive result when applied to a person suffering from a certain disease, and a probability0.10 of giving a (false) positive when applied to a non-sufferer. It is estimated that 0.5 % of the population are sufferers. Suppose that the test is now administered to a person about whom we have no relevant information relating to the disease (apart from the fact that he/she comes from this population). Calculate the following probabilities: that the test result will be positive",
		"hint": "Remember that you are calculating the probability of P(Black or 6). Start of by calculating the probability of selecting a black card, then selecting a 6",
		"options":[
			{
				"optionTxt": " 0.10425",
				"answer": true
			},
			{
				"optionTxt": "0.95",
				"answer": false
			},
			{
				"optionTxt": "0.00047",
				"answer": false
			},
			{
				"optionTxt": "0.05",
				"answer": false
			}
		],
		"feedback":"P(T) = P(T|S)P(S) + P(T|S)P(S) = (0.95 × 0.005) + (0.1 × 0.995) = 0.10425"
	},
	{
		"id":"q6",
		"topic":"Bayesian Theory",
		"weight":3,
		"questionTxt": "A diagnostic test has a probability 0.95 of giving a positive result when applied to a person suffering from a certain disease, and a probability0.10 of giving a (false) positive when applied to a non-sufferer. It is estimated that 0.5 % of the population are sufferers. Suppose that the test is now administered to a person about whom we have no relevant information relating to the disease (apart from the fact that he/she comes from this population). Calculate the following probabilities: that the test result will be positive",
		"hint": "Remember that you are calculating the probability of P(Black or 6). Start of by calculating the probability of selecting a black card, then selecting a 6",
		"options":[
			{
				"optionTxt": " 0.0060",
				"answer": false
			},
			{
				"optionTxt": "0.165",
				"answer": true
			},
			{
				"optionTxt": "0.0000059",
				"answer": false
			},
			{
				"optionTxt": "0.00593",
				"answer": false
			}
		],
		"feedback":"(0.99 * 0.001)/0.005985 = 0.165"
	}
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
