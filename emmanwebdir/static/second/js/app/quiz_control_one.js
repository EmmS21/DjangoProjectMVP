var star = '<svg id="star" x="0px" y="0px" viewBox="0 0 512.001 512.001"><path fill="#ffdc64" d="M499.92 188.26l-165.84-15.38L268.2 19.9c-4.6-10.71-19.8-10.71-24.4 0l-65.88 152.97-165.84 15.38c-11.61 1.08-16.3 15.52-7.54 23.22L129.66 321.4 93.04 483.87c-2.56 11.38 9.73 20.3 19.75 14.35L256 413.2l143.2 85.03c10.03 5.96 22.32-2.97 19.76-14.35L382.34 321.4l125.12-109.92c8.77-7.7 4.07-22.14-7.54-23.22z"/><path fill="#ffc850" d="M268.2 19.91c-4.6-10.71-19.8-10.71-24.4 0l-65.88 152.97-165.84 15.38c-11.61 1.08-16.3 15.52-7.54 23.22L129.66 321.4 93.04 483.87c-2.56 11.38 9.73 20.3 19.75 14.35l31.97-18.98c4.42-182.1 89.03-310.33 156.02-383.7L268.2 19.92z"/></svg>';

//Initialisation of variables
var currentQuestion = -1;
var tokens = 200;

var questions =[
	{
		"id":"q0",
		"topic":"Probability: Intro",
		"weight":2,
		"questionTxt": "Assume we are a company that sells solar panels to other businesses. We ship 30% of the products to Company A in Ghana and 70% of our products to company B in Uganda. Company A reports that 5% of our products are defective and company B reports that 4% of our products are defective. Find the probability that a solar panel that is sent to Company A is defective?",
		"hint": "What is the proportion of our solar panels are shipped to Company A? What is the probability that Company A reports that our solar panels are defective?",
		"options":[
			{
				"optionTxt": "0.030",
				"answer": false
			},
			{
				"optionTxt": "0.30",
				"answer": false
			},
			{
				"optionTxt": "0.1667",
				"answer": false
			},
			{
				"optionTxt": "0.015",
				"answer": true
			}
		],
		"feedback":"P(A)  = P(D|A)=  0.3    0.3(0.05)= 0.015"
	},
	{
		"id":"q1",
		"topic":"Probability: Intro",
		"weight":2,
		"questionTxt": "A couple has two children. Let’s assume that the gender of these children is equally likely to be male or female. What is the probability that this couple has two girls, assuming atleast one of their children is a girl?",
		"hint": "How does the reduced sample size change your calculation?",
		"options":[
			{
				"optionTxt": "1/6",
				"answer": false
			},
			{
				"optionTxt": "1/3",
				"answer": true
			},
			{
				"optionTxt": "1/2",
				"answer": false
			},
			{
				"optionTxt": "2/3",
				"answer": false
			}
		],
		"feedback":"P(2 girls| 1 girl) = num of children in reduced sample space with two girls/num of elements in reduced sample space  = 1/3."
	},
	{
		"id":"q2",
		"topic":"Probability: Intro",
		"weight":1,
		"questionTxt": "Our factory produces car parts that are either good (90%), slightly defective (2%), or obviously defective (8%). Car parts that have been produced pass through an automatic inspection machine, which is able to detect any part that is obviously defective and discard it. What is the quality of the parts that make it through the inspection machine and get shipped?",
		"hint": "Calculate the probability that we produce a good car part and the probability that we produce a car part that is not obviously defective?",
		"options":[
			{
				"optionTxt": "0.978",
				"answer": true
			},
			{
				"optionTxt": "0.0869",
				"answer": false
			},
			{
				"optionTxt": "0.072",
				"answer": false
			},
			{
				"optionTxt": "1",
				"answer": false
			}
		],
		"feedback":"P(Good|OD) = P(Good)/ 1 - P(OD) = 0.90/1-0.08 = 90/92 = 0.978"
	},
	{
		"id":"q3",
		"topic":"Probability: Intro",
		"weight":3,
		"questionTxt": "We are going to roll a fair, six sided dice once. What is the probability that a 4 was rolled, assuming that an odd number has been rolled?",
		"hint": "Remember to reduce the sample size when carrying out your calculations",
		"options":[
			{
				"optionTxt": "1/6",
				"answer": false
			},
			{
				"optionTxt": "2/3",
				"answer": false
			},
			{
				"optionTxt": "1/3",
				"answer": true
			},
			{
				"optionTxt": "5/6",
				"answer": false
			}
		],
		"feedback":"P(4 | even) =  Number of 4’s in the reduced space/Number of elements in reduced space = 1/3"
	},
	{
		"id":"q4",
		"topic":"Probability: Intro",
		"weight":3,
		"questionTxt": "We have a bag that contains blue and purple marbles. We draw two marbles without replacing them. The probability of selecting a blue marble and then a purple marble is 0.28. The probability of selecting a blue marble on the first draw is 0.5. What is the probability of selecting a purple marble on the second draw, assuming that the first marble drawn was blue?",
		"hint": "P(purple and blue)/p(blue)",
		"options":[
			{
				"optionTxt": "0.014",
				"answer": false
			},
			{
				"optionTxt": "0.056",
				"answer": false
			},
			{
				"optionTxt": "0.14",
				"answer": false
			},
			{
				"optionTxt": "0.562",
				"answer": true
			}
		],
		"feedback":"P(purple|blue) = P(purple and blue)/P(blue) = 0.28/0.5 = 0.56."
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
