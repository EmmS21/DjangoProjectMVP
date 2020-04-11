var star = '<svg id="star" x="0px" y="0px" viewBox="0 0 512.001 512.001"><path fill="#ffdc64" d="M499.92 188.26l-165.84-15.38L268.2 19.9c-4.6-10.71-19.8-10.71-24.4 0l-65.88 152.97-165.84 15.38c-11.61 1.08-16.3 15.52-7.54 23.22L129.66 321.4 93.04 483.87c-2.56 11.38 9.73 20.3 19.75 14.35L256 413.2l143.2 85.03c10.03 5.96 22.32-2.97 19.76-14.35L382.34 321.4l125.12-109.92c8.77-7.7 4.07-22.14-7.54-23.22z"/><path fill="#ffc850" d="M268.2 19.91c-4.6-10.71-19.8-10.71-24.4 0l-65.88 152.97-165.84 15.38c-11.61 1.08-16.3 15.52-7.54 23.22L129.66 321.4 93.04 483.87c-2.56 11.38 9.73 20.3 19.75 14.35l31.97-18.98c4.42-182.1 89.03-310.33 156.02-383.7L268.2 19.92z"/></svg>';

//Initialisation of variables
var currentQuestion = -1;
var tokens = 200;

var questions =[
	{
		"id":"q0",
		"topic":"Probability: Intro",
		"weight":2,
		"questionTxt": "A 'die', the singular of dice, is a cube with six faces numbered 1, 2, 3, 4, 5, and 6. What is the chance of getting 1 when rolling a die?",
		"hint": "Remember that probability is the likelihood of an event occurring measured by the ratio of the favourable cases to the whole number of cases possible",
		"options":[
			{
				"optionTxt": "2/6",
				"answer": false
			},
			{
				"optionTxt": "1/6",
				"answer": true
			},
			{
				"optionTxt": "1/3",
				"answer": false
			},
			{
				"optionTxt": "1/9",
				"answer": false
			}
		],
		"feedback":" There is a 1/6 probability for each number that appears on the die."
	},
	{
		"id":"q1",
		"topic":"Probability: Intro",
		"weight":2,
		"questionTxt": "What is the chance of getting a 1 or 2 in the next roll?",
		"hint": "How do we factor in both probabilities?",
		"options":[
			{
				"optionTxt": "1/3",
				"answer": true
			},
			{
				"optionTxt": "1/6",
				"answer": false
			},
			{
				"optionTxt": "3/6",
				"answer": false
			},
			{
				"optionTxt": "2/3",
				"answer": false
			}
		],
		"feedback":" 1 and 2 constitute two of the six equally likely possible outcomes, so the chance of getting one of these two outcomes must be 2/6 = 1/3."
	},
	{
		"id":"q2",
		"topic":"Probability: Intro",
		"weight":1,
		"questionTxt": "A fair die is thrown once. What is the probability that the number obtained is a multiple of 2?",
		"hint": "How many numbers between 1 and 6 are multiples of 2?",
		"options":[
			{
				"optionTxt": "1/2",
				"answer": true
			},
			{
				"optionTxt": "2/6",
				"answer": false
			},
			{
				"optionTxt": "4/6",
				"answer": false
			},
			{
				"optionTxt": "1/6",
				"answer": false
			}
		],
		"feedback":"The multiples of 2 between 1 and 6 are; 2,4 & 6. p(multiple of 2) = 3/6 or 1/2."
	},
	{
		"id":"q3",
		"topic":"Probability: Intro",
		"weight":3,
		"questionTxt": "There are 6 male and 9 female students in a school in Nigeria. Half of these male students and 5 of the female students are in the African languages class. A student is picked at random to take a photo of the class. Find the probability that this student is male.",
		"hint": "Re-read the question and identify what is being asked",
		"options":[
			{
				"optionTxt": "3/8",
				"answer": false
			},
			{
				"optionTxt": "9/15",
				"answer": false
			},
			{
				"optionTxt": "6/15",
				"answer": true
			},
			{
				"optionTxt": "6/9",
				"answer": false
			}
		],
		"feedback":"We want the probability of picking a random male student in a group of 15 students. The probability is therefore 6/15."
	},
	{
		"id":"q4",
		"topic":"Probability: Intro",
		"weight":3,
		"questionTxt": "What is the probability of throwing two dies and getting the sum of the fallen numbers that is greater than or equal to 3",
		"hint": "If you turn both dies into pairs of numbers between 1 and 6, how many of those pairs would add up to a number greater than or equal to 3?",
		"options":[
			{
				"optionTxt": "10/12",
				"answer": false
			},
			{
				"optionTxt": "9/12",
				"answer": false
			},
			{
				"optionTxt": "8/12",
				"answer": false
			},
			{
				"optionTxt": "11/12",
				"answer": true
			}
		],
		"feedback":"There are is only 1 possible combination where the sum of the rolls would be less than 3, that is 1 and 1, therefore out of all 12 possible combinations 11/12 would be greater than or equal 3."
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
